# Python-telegram-bot

The telegram.ext submodule is built on top of the pure API implementation. It provides an easy-to-use interface and takes some work off the programmer, so you don't have to repeat yourself.

It consists of several classes, but the most important one is telegram.ext.Application.

The Application class is responsible for fetching updates from the update_queue, which is where the Updater class continuously fetches new updates from Telegram and adds them to this queue. If you create an Application object, using ApplicationBuilder, it will automatically create a Updater for you and link them together with an asyncio.Queue. You can then register handlers of different types in the Application, which will sort the updates fetched by the Updater according to the handlers you registered, and deliver them to a callback function that you defined.

Every handler is an instance of any subclass of the telegram.ext.BaseHandler class. The library provides handler classes for almost all use cases, but if you need something very specific, you can also subclass Handler yourself.

To begin, you'll need an Access Token. If you have already read and followed Introduction to the API, you can use the one you generated then. If not: To generate an Access Token, you have to talk to @BotFather and follow a few simple steps (described here). You should really read the introduction first, though.