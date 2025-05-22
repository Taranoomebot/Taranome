# main_logic.py

from telegram import Update
from telegram.ext import ContextTypes

async def handle_new_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ دریافت پیام جدید در کانال")
    # این تابع برای تست فقط لاگ می‌زنه
    # چون پیام‌های کانال به کاربر پاسخ داده نمی‌شن

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ دریافت callback")
    await update.callback_query.answer("دکمه کلیک شد!")
