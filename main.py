import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("InstaMarkret 24/7 кор мекунад ✅\n/start -ро пахш кун")

async def echo(update, context):
    await update.message.reply_text(f"Паёматро гирифтам: {update.message.text}")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
app.run_polling()
