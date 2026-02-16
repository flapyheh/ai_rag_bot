import logging
from aiogram import Bot, Dispatcher

from config.config import BOT_TOKEN, OPENAI_API_TOKEN

logger = logging.getLogger(__name__)

async def main() -> None:
    logger.info('Создаем бота')
    bot = Bot(BOT_TOKEN)
    
    logger.info('Создаем диспечера')
    dp = Dispatcher()