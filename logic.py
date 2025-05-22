from telegram import Update
from telegram.ext import ContextTypes

async def handle_new_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("🔔 New post received in channel:")
    print(update.channel_post.text if update.channel_post else "No text")

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("📲 Callback query received:")
    print(update.callback_query.data if update.callback_query else "No data")
