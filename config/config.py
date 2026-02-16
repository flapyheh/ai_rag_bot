import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_TOKEN = os.getenv("OPENAI_API_TOKEN")

LOG_LEVEL = os.getenv('LOG_LEVEL')
LOG_FORMAT = os.getenv('LOG_FORMAT')