#https://github.com/vo0x
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import wikipedia
import trengine
from db import register_user, get_all_users, get_user_count
from config import owner_id
engine = trengine.AsyncEngine()

async def start(u: Update, c: ContextTypes.DEFAULT_TYPE):
    user_firstname = u.message.from_user.first_name
    user = u.message.from_user
    register_user(user.id, user.username, user.first_name, user.last_name)
    keyboard = [
        [
            InlineKeyboardButton("search 🔎", callback_data = "search"),
            InlineKeyboardButton("translator 🔠", callback_data = "translate")
        ],
        [InlineKeyboardButton("source code", url= "https://github.com/vo0x")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await u.effective_message.reply_text(
        f"- welcome {user_firstname} to the wikiwrite telegram bot 👋\n- here you can search/translate and do another cool things 😁",
        reply_markup=reply_markup,
        quote=True
    )
    c.user_data["state"] = None

async def broadcast(u: Update, c: ContextTypes.DEFAULT_TYPE ):
    if str(u.message.chat_id) != str(owner_id):
        await u.message.reply_text(
            "your not authorized to use this command",
            quote=True
        )
        return
    try:
        message = " ".join(c.args)
        users = get_all_users()
        for user in users:
            try:
                await c.bot.send_message(
                    chat_id=user,
                    text=message
                )
            except Exception as e:
                print(f"Failed to send message to {user}: {e}")
        
    except IndexError:
        await u.message.reply_text("Usage: /broadcast <message>")

async def stats(u: Update, c: ContextTypes.DEFAULT_TYPE):
    count = get_user_count()
    await u.message.reply_text(f"Total bot users: {count}")

async def search(search_query: str) -> str:
    try:
        result = wikipedia.summary(search_query)
        return result
    except:
        error = "Error"
        return error




async def translate(text) :
   
    result = await engine.google.translate(text, "en")
    return result
    