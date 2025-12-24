from telegram.ext import (
    ApplicationBuilder, CommandHandler,
    CallbackQueryHandler, ConversationHandler,
    MessageHandler, filters
)
from config import BOT_TOKEN
from start import start
from help import help_cmd
from clone import clone_start, get_token, GET_TOKEN

app = ApplicationBuilder().token(BOT_TOKEN).build()

clone_conv = ConversationHandler(
    entry_points=[CallbackQueryHandler(clone_start, pattern="clone")],
    states={
        GET_TOKEN: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_token)]
    },
    fallbacks=[]
)

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(clone_conv)

print("Bot is running...")
app.run_polling()
