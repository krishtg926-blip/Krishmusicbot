from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, filters

GET_TOKEN = 1

async def clone_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        "♻️ Clone Bot\n\n"
        "Apna Bot Token bhejo (BotFather se mila hua).\n\n"
        "⚠️ Token safe rahega."
    )
    return GET_TOKEN

async def get_token(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = update.message.text.strip()

    if ":" not in token:
        await update.message.reply_text("❌ Invalid token, dobara bhejo.")
        return GET_TOKEN

    await update.message.reply_text(
        "✅ Token received!\n"
        "Clone process start ho gaya 🚀"
    )

    return ConversationHandler.END
