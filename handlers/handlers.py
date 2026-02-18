import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import faiss

from rag.ai_service import generate_answer

logger = logging.getLogger(__name__)
handler_router = Router()

@handler_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer('Доброго времени суток! Это FAQ AI бот.\nЗадайте любой вопрос по поводу работы этого бота!')
    
@handler_router.message()
async def process_question(message: Message, chunks : list[str], index : faiss.IndexFlatL2):
    try:
        responce = await generate_answer(index=index, chunks=chunks, query=message.text)
        await message.answer(text=responce)
    except Exception as e:
        logger.warning(e)
        await message.answer('Что-то случилось и мы не можем дать вам ответ. Спросите чуть позже')