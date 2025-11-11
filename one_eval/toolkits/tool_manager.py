from typing import Any, Dict, Callable
import asyncio
from dataflow_agent.logger import get_logger

log = get_logger(__name__)

class ToolManager:
    """工具管理器"""
    def __init__(self):
        # 全局工具
        self.tools: Dict[str, Callable] = {}
        # 角色区分的工具
        self.role_tools: Dict[str, Dict[str, Callable]] = {}

    def register_tool(self, name: str, func: Callable):
        self.tools[name] = func
        log.info(f"Registered tool: {name}")

    def register_custom_tool(self, name: str, func, role: str = None, override: bool = False):
        """注册自定义工具，可按角色分类"""
        if role:
            if role not in self.role_tools:
                self.role_tools[role] = {}
            if not override and name in self.role_tools[role]:
                log.warning(f"Tool '{name}' already exists for role '{role}', skipped.")
                return
            self.role_tools[role][name] = func
            log.info(f"Registered custom tool '{name}' for role '{role}'")
        else:
            if not override and name in self.tools:
                log.warning(f"Global tool '{name}' already exists, skipped.")
                return
            self.tools[name] = func
            log.info(f"Registered global custom tool: {name}")

    def get_tool(self, name: str, role: str = None) -> Callable:
        if role and role in self.role_tools and name in self.role_tools[role]:
            return self.role_tools[role][name]
        return self.tools[name]

    async def execute(self, name: str, *args, role: str = None, **kwargs) -> Any:
        func = self.get_tool(name, role)
        if asyncio.iscoroutinefunction(func):
            return await func(*args, **kwargs)
        return func(*args, **kwargs)


_tool_manager = None

def get_tool_manager() -> ToolManager:
    global _tool_manager
    if _tool_manager is None:
        _tool_manager = ToolManager()
    return _tool_manager
