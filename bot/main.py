# https://github.com/vo0x
import telegram
from telegram import Update
from telegram.ext import(
    CommandHandler,
    CallbackQueryHandler,
    Application,
    MessageHandler,
    filters
)
import logging

from utils import start, broadcast, stats
from handlers import main_handler
from db import init_db
from config import bot_token

from callback import *

logging.basicConfig(

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO

)

# set higher logging level for httpx to avoid all GET and POST requests being logged

logging.getLogger("httpx").setLevel(logging.WARNING)


logger = logging.getLogger(__name__)

def main():
    init_db()
    app = Application.builder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("stats", stats))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, main_handler))
    app.add_handler(CallbackQueryHandler(search_button, pattern="search"))
    app.add_handler(CallbackQueryHandler(translate_button, pattern="translate"))
    app.add_handler(CallbackQueryHandler(back, pattern="back"))

    app.run_polling()
if __name__ == "__main__":
    main()