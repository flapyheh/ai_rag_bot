import asyncio
import faiss
import numpy as np
from openai import AsyncOpenAI

from config.config import OPENAI_API_TOKEN
from models.embedding_model import model
from rag.index import index

client = AsyncOpenAI(api_key= OPENAI_API_TOKEN)

async def search(index : faiss.IndexFlatL2, chunks : list[str], query : str, k : int = 3) -> list[str]:
    #embedding запроса
    query_vector = await asyncio.to_thread(
        model.encode,
        [query]
    )
    query_vector = np.array(query_vector).astype("float32")
    
    #поиск самых похожих чанков на поиск
    distances, indices = await asyncio.to_thread(
        index.search,
        query_vector,
        k
    )
    
    results = []
    
    for i in indices[0]:
        results.append(chunks[i])  
    return results

async def generate_answer(index : faiss.IndexFlatL2, chunks : list[str], query : str) -> str:
    
    context_chunks = await search(index=index, chunks=chunks, query=query)
    
    context_text = "\n".join(context_chunks)
    
    prompt = f"""
Ты AI ассистент.

Отвечай только на основе контекста.

Контекст:
{context_text}

Вопрос:
{query}

Ответ:
"""

    responce = await client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 0.2
    )
    return responce.choices[0].message.content