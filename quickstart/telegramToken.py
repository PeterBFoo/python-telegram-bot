
import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('quickstart/token.env')

def get(key):
    load_dotenv(dotenv_path=dotenv_path)


    BOT_TOKEN = os.getenv('BOT_TOKEN')
    GOOGLE_API_TOKEN = os.getenv('GOOGLE_TOKEN')

    if key == "BOT_TOKEN":
        return BOT_TOKEN
    elif key == "GOOGLE_TOKEN":
        return GOOGLE_API_TOKEN

