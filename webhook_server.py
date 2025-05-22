from flask import Flask, request
from telegram import Update
from telegram.ext import Application
import os

TOKEN = "7908277919:AAHNhrZgRpdPj5LdX5lI0Chx8u4L4VjgO2w"
WEBHOOK_PATH = f"/webhook/{TOKEN}"

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

from telegram.ext import MessageHandler, filters, CallbackQueryHandler
from main_logic import handle_new_post, handle_callback

application.add_handler(MessageHandler(filters.ALL & filters.ChatType.CHANNEL, handle_new_post))
application.add_handler(CallbackQueryHandler(handle_callback))

@app.get("/")
def index():
    return "🚀 Bot is running!"

@app.post(WEBHOOK_PATH)
async def webhook() -> str:
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return 'OK'

if __name__ == "__main__":
    print("✅ Flask webhook server running...")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
