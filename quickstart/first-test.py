from telegramToken import getToken

import asyncio
import telegram

async def main():
    bot = telegram.Bot(getToken())
    async with bot:
        print(await bot.get_me()) # Prints the bot's name and username

if __name__ == "__main__":
    asyncio.run(main())