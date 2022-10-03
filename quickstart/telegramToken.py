import os
from dotenv import load_dotenv

file = "python-telegram-bot\quickstart\config.env"

def getToken():
    load_dotenv(file)
    token = os.getenv("TOKEN")

    if not token:
        raise Exception(f"Couldn't read file {file}")
    else:
        return token
