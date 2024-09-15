# https://github.com/vo0x
import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from utils import search, translate
import json

SEARCH, TRANSLATE = range(2)

async def serach_handler(u: Update, c: ContextTypes.DEFAULT_TYPE):
    serach_query = u.effective_message.text
    result = await search(serach_query)

    keyboard = [
        [
            InlineKeyboardButton("back", callback_data="back")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await u.effective_message.reply_text(
        f"{result}",
        reply_markup=reply_markup,
        quote=True
    )
async def translate_handler(u: Update, c: ContextTypes.DEFAULT_TYPE):
    text = u.effective_message.text

    result = await translate(text)
    json_result = str(result)
    data = json.loads(json_result)


    translated_text = data['translated_text']
    original_language = data['original_language']
    dest_language = data['dest_language']
    
    
  
    formatted_message = (
        f"Original Language: {original_language.upper()}\n"
        f"Destination Language -> {dest_language.upper()}\n"
        f"Translated Text => {translated_text}"
    )
    keyboard =[ 
        [
            InlineKeyboardButton("back", callback_data="back")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await u.effective_message.reply_text(
        f"{formatted_message}",
        reply_markup=reply_markup,
        quote=True
    )
    
async def main_handler(u: Update, c: ContextTypes.DEFAULT_TYPE):
    if c.user_data["state"] == SEARCH:
        await serach_handler(u, c)
    elif c.user_data["state"] == TRANSLATE:
        await translate_handler(u, c)
    else:
        pass
