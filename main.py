import asyncio
import logging

from config.config import LOG_LEVEL,LOG_FORMAT
from bot.bot import main

logging.basicConfig(
    level=logging.getLevelName(level=LOG_LEVEL),
    format=LOG_FORMAT,
)

asyncio.run(main())