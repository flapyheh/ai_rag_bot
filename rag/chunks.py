import logging

logger = logging.getLogger(__name__)
chunks = []

def load_database(file: str='db/database.txt', max_chunk_size = 300) -> list[str]:
    logger.info('Начинаем загрузку чанков')
    global chunks
    
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
        
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        #если чанк не переполнен
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + '. '
        #иначе добавление в массив и равен 
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + '. '
            
    #добавить последний чанк
    if current_chunk:
        chunks.append(current_chunk)
        
    logger.info('Чанки загружены')
    return chunks