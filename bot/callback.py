import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from handlers import SEARCH, TRANSLATE

async def search_button(u: Update, c: ContextTypes.DEFAULT_TYPE):
    query = u.callback_query

    keyboard = [
        [
            InlineKeyboardButton("back", callback_data="back")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("send me query to search", reply_markup=reply_markup)

    c.user_data['state'] = SEARCH

async def translate_button(u: Update, c: ContextTypes.DEFAULT_TYPE):
    query = u.callback_query

    keyboard = [
        [
            InlineKeyboardButton("back", callback_data="back")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("send me a text to translate it for you ", reply_markup=reply_markup)

    c.user_data['state'] = TRANSLATE

async def back(u: Update, c: ContextTypes.DEFAULT_TYPE):
   
    query = u.callback_query 
    user_firstname = query.message.from_user.first_name
    keyboard = [
        [
            InlineKeyboardButton("search 🔎", callback_data = "search"),
            InlineKeyboardButton("translator 🔠", callback_data = "translate")
        ],
        [InlineKeyboardButton("source code", url= "https://github.com/vo0x")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        f"- welcome {user_firstname} to the wikiwrite telegram bot 👋\n- here you can search/translate and do another cool things 😁",
        reply_markup=reply_markup
    )

    c.user_data["state"] = None