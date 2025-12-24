from telegram import Update
from telegram.ext import ContextTypes

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 Available Commands:\n\n"
        "/start - Start bot\n"
        "/help - Show help menu\n\n"
        "More music commands coming soon..."
    )
