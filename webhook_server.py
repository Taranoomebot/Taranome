from flask import Flask, request
from telegram import Update
from telegram.ext import Application
import os

TOKEN = "7908277919:AAHNhrZgRpdPj5LdX5lI0Chx8u4L4VjgO2w"
WEBHOOK_PATH = f"/webhook/{TOKEN}"

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# هندلرهای ربات رو اینجا اضافه کن
from telegram.ext import MessageHandler, filters, CallbackQueryHandler

# فرضا اینها تو همین فایل باشن یا ایمپورت کنی
async def handle_new_post(update, context):
    # کدت اینجا
    pass

async def handle_callback(update, context):
    # کدت اینجا
    pass

application.add_handler(MessageHandler(filters.ALL & filters.ChatType.CHANNEL, handle_new_post))
application.add_handler(CallbackQueryHandler(handle_callback))


@app.get("/")
def index():
    return "🚀 Bot is running!"


@app.route(WEBHOOK_PATH, methods=["GET", "POST"])
async def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), application.bot)
        await application.process_update(update)
        return "OK"
    else:
        return "This endpoint accepts POST requests only.", 405


if __name__ == "__main__":
    print("✅ Flask webhook server running...")
    app.run(host="0.0.0.0", port=10000)
