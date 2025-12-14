import sys
from loguru import logger

from src.core.config import settings

logger.add(
    sys.stdout,
    level=settings.LOG_LEVEL,
    enqueue=True,
    colorize=True,
)
