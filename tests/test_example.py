from one_eval.core.state import NodeState
from one_eval.core.graph import GraphBuilder
from one_eval.nodes.nl2bench_node import NL2BenchNode
from one_eval.nodes.eval_node import EvalNode
import asyncio

async def main():
    # 使用 GraphBuilder 来构建图
    builder = GraphBuilder(state_model=NodeState, entry_point="nl2bench")
    
    # 添加节点
    builder.add_node("nl2bench", NL2BenchNode(), role="nl2bench")
    builder.add_node("eval", EvalNode(), role="eval")
    
    # 添加边
    builder.add_edge("nl2bench", "eval")
    
    # 构建并编译图
    graph = builder.build()
    
    # 创建初始状态并运行
    initial_state = NodeState()
    # 可以根据需要设置初始状态的属性
    # initial_state.user_query = "请评测这个模型的数学能力"
    
    # 运行图
    result = await graph.ainvoke(initial_state)
    print("测试执行完成，结果:", result)

if __name__ == "__main__":
    asyncio.run(main())
