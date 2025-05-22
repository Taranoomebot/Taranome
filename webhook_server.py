# webhook_server.py

from flask import Flask, request
from telegram import Update
from telegram.ext import Application, MessageHandler, CallbackQueryHandler, filters

# توکن رو مستقیم وارد کن (موقتی برای تست)
TOKEN = "7908277919:AAHNhrZgRpdPj5LdX5lI0Chx8u4L4VjgO2w"
WEBHOOK_PATH = f"/webhook/{TOKEN}"

# آدرس عمومی دامنه‌ات در Render
YOUR_PUBLIC_DOMAIN = "https://taranome.onrender.com"
WEBHOOK_URL = f"https://taranome.onrender.com{WEBHOOK_PATH}"


# Flask app
app = Flask(__name__)

# ساخت اپلیکیشن تلگرام
application = Application.builder().token(TOKEN).build()

# ایمپورت هندلرهای اصلی
from main_logic import handle_new_post, handle_callback

# اضافه کردن هندلرها
application.add_handler(MessageHandler(filters.ALL & filters.ChatType.CHANNEL, handle_new_post))
application.add_handler(CallbackQueryHandler(handle_callback))

# دریافت آپدیت‌ها از وبهوک
@app.post(WEBHOOK_PATH)
async def webhook() -> str:
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return 'OK'

# اجرای سرور و ثبت وبهوک هنگام اجرا
if __name__ == "__main__":
    print("✅ Flask webhook server running...")

    import asyncio
    async def set_webhook():
        await application.bot.set_webhook(WEBHOOK_URL)
        print("✅ Webhook تنظیم شد:", WEBHOOK_URL)

    asyncio.get_event_loop().run_until_complete(set_webhook())

    app.run(host="0.0.0.0", port=8443)
