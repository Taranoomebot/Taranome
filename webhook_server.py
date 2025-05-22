import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, MessageHandler, CallbackQueryHandler, filters
from main_logic import handle_new_post, handle_callback  # تو این فایل تابع‌ها باید تعریف شده باشن

# تنظیمات ثابت
TOKEN = "7908277919:AAHNhrZgRpdPj5LdX5lI0Chx8u4L4VjgO2w"
WEBHOOK_URL = "https://taranome.onrender.com"
WEBHOOK_PATH = f"/webhook/{TOKEN}"

# ساخت اپلیکیشن Flask و بات
app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

# اضافه کردن هندلرها
application.add_handler(MessageHandler(filters.ALL & filters.ChatType.CHANNEL, handle_new_post))
application.add_handler(CallbackQueryHandler(handle_callback))

@app.post(WEBHOOK_PATH)
async def webhook() -> str:
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return 'OK'

# اجرای سرور Flask
if __name__ == "__main__":
    print("✅ Flask webhook server running...")

    # ست کردن webhook موقع راه‌اندازی
    import asyncio
    async def set_webhook():
        await application.bot.set_webhook(url=f"{WEBHOOK_URL}{WEBHOOK_PATH}")

    asyncio.run(set_webhook())

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
