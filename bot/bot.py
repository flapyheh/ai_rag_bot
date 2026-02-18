import logging
from aiogram import Bot, Dispatcher

from config.config import BOT_TOKEN, OPENAI_API_TOKEN
from rag.chunks import load_database
from rag.index import create_index
from handlers.handlers import handler_router

logger = logging.getLogger(__name__)

async def main() -> None:
    bot = Bot(BOT_TOKEN)
    logger.info('Запускаем бота')    
    dp = Dispatcher()
    logger.info('Создаем диспечера')
    
    chunks = load_database()
    index = await create_index(chunks=chunks)
    
    logger.info('Добавляем роутер')
    dp.include_router(handler_router)
    
    try:
        await dp.start_polling(
            bot, 
            chunks=chunks,
            index=index
        )
    except Exception as e:
        logger.exception(e)