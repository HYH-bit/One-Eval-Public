import logging
import os
from logging.handlers import RotatingFileHandler

# === 默认配置 ===
LOG_FILE = os.getenv("ONE_EVAL_LOG_FILE", "one_eval.log")
LOG_LEVEL = os.getenv("ONE_EVAL_LOG_LEVEL", "INFO").upper()
MAX_SIZE = 10 * 1024 * 1024
BACKUP_COUNT = 3

# === 颜色映射 ===
COLOR = {
    "DEBUG": "\033[36m",     # 青色
    "INFO": "\033[32m",      # 绿色
    "WARNING": "\033[33m",   # 黄色
    "ERROR": "\033[31m",     # 红色
    "CRITICAL": "\033[41m\033[37m",  # 红底白字
    "RESET": "\033[0m",
}
FIELD = {
    "time": "\033[90m",
    "name": "\033[35m",
    "loc": "\033[94m",
}

class ColorFormatter(logging.Formatter):
    def format(self, record):
        reset = COLOR["RESET"]
        return (
            f"{FIELD['time']}{self.formatTime(record)}{reset} | "
            f"{COLOR.get(record.levelname, '')}{record.levelname:<8}{reset} | "
            f"{FIELD['name']}{record.name}{reset} | "
            f"{FIELD['loc']}{record.filename}:{record.lineno}{reset} | "
            f"{COLOR.get(record.levelname, '')}{record.getMessage()}{reset}"
        )

def _make_handlers():
    console = logging.StreamHandler()
    console.setLevel(LOG_LEVEL)
    console.setFormatter(ColorFormatter("%Y-%m-%d %H:%M:%S"))

    file = RotatingFileHandler(LOG_FILE, maxBytes=MAX_SIZE, backupCount=BACKUP_COUNT, encoding="utf-8")
    file.setLevel(LOG_LEVEL)
    file.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    ))
    return [console, file]

def get_logger(name: str = "one_eval") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        for h in _make_handlers():
            logger.addHandler(h)
        logger.setLevel(LOG_LEVEL)
        logger.propagate = False
    return logger

log = get_logger()

if __name__ == "__main__":
    log.info("Logger ready.")
    log.warning("Warning example.")
    log.error("Error example.")
