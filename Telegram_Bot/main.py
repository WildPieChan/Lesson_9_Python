from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import configure
from bot_commands import *


app = ApplicationBuilder().token(configure.config['token']).build()

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calculator_command))

app.run_polling()