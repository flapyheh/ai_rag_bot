import logging
import asyncio
import faiss
import numpy as np

from models.embedding_model import model

logger = logging.getLogger(__name__)

index = None

async def create_index(chunks : list[str]) -> None:
    global index
    
    embeddings = await asyncio.to_thread(model.encode, chunks)
    embeddings = np.array(embeddings).astype('float32')
    
    dimension = embeddings.shape[1]
    
    index = faiss.IndexFlatL2(dimension)
    
    index.add(dimension)
    logger.info("Создали faiss index")