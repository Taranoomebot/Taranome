# webhook_server.py

from flask import Flask, request
from telegram import Update
from telegram.ext import Application

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = f"/webhook/{TOKEN}"

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# هندلرهای ربات رو اینجا اضافه کن (مثل handle_new_post، handle_callback و ...)
from telegram.ext import MessageHandler, filters, CallbackQueryHandler
from main_logic import handle_new_post, handle_callback  # ماژول تو

application.add_handler(MessageHandler(filters.ALL & filters.ChatType.CHANNEL, handle_new_post))
application.add_handler(CallbackQueryHandler(handle_callback))

@app.post(WEBHOOK_PATH)
async def webhook() -> str:
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return 'OK'

if __name__ == "__main__":
    print("✅ Flask webhook server running...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

