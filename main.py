from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот на Render.")

if __name__ == "__main__":
    application = ApplicationBuilder().token("8055164066:AAHu-LghWaz9PVdJBGbLk8itdjA2-jhqYOg").build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
