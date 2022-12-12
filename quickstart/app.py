import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from pyyoutube import Api as yt
from telegramToken import get

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Run this commands with the following instructions: \n /youtube -> Search a keyword on Youtube searcher and get the URL")

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userRequest = update.message.text[8::]

    if not userRequest.replace(" ", ""):
        return await  context.bot.send_message(chat_id=update.effective_chat.id, text="Please, introduce a keyword to make a search")

    api = yt(api_key=get("GOOGLE_TOKEN"))
    search_response = api.search_by_keywords(q=userRequest, search_type=["video"], count=1, limit=1)
    url = "https://www.youtube.com/watch?v="

    for search_result in search_response.items:
        if search_result.id.kind == "youtube#video":
            url = url + search_result.id.videoId
            await context.bot.send_message(chat_id=update.effective_chat.id, text=url)

async def playlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    userRequest = update.message.text[9::]

    if not userRequest.replace(" ", ""):
        return await  context.bot.send_message(chat_id=update.effective_chat.id, text="Please, introduce a keyword to make a search")


    api = yt(api_key=get("GOOGLE_TOKEN"))
    search_response = api.search_by_keywords(q=userRequest, search_type=["playlist"], count=1, limit=1)
    url = "https://www.youtube.com/watch?v="

    for search_result in search_response.items:
        if search_result.id.kind == "youtube#playlist":
            url = url + search_result.id.playlistId
            await context.bot.send_message(chat_id=update.effective_chat.id, text=url)


async def unknownCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

async def unknownMedia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="¿What is that file? I can't use any of these files for any purpose :c.")

def getHandlers():
    return [CommandHandler('start', start), CommandHandler('youtube', youtube),
    CommandHandler('playlist', playlist), MessageHandler(filters.COMMAND, unknownCommand),MessageHandler(filters.VIDEO | filters.PHOTO | filters.Document.ALL, unknownMedia)]

if __name__ == '__main__':
    application = ApplicationBuilder().token(get("BOT_TOKEN")).build()
    for handler in getHandlers():
        application.add_handler(handler)
    application.run_polling()