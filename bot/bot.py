import logging
from aiogram import Bot, Dispatcher

from config.config import BOT_TOKEN, OPENAI_API_TOKEN

logger = logging.getLogger(__name__)

async def main() -> None:
    bot = Bot(BOT_TOKEN)
    logger.info('Создаем бота')
    
    dp = Dispatcher()
    logger.info('Создаем диспечера')
    
    