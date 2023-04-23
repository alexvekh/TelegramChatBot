from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

BOT_TOKEN = "5966711758:AAHRksaeQ0-AsYvpo_mSX1QFS6gAHQx52pk"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hi here! \n This is simle bot.")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("What is your question?")


def run():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))

    application.run_polling()


if __name__ == "__main__":
    run()
