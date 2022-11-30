from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ApplicationBuilder
import datetime as dt

def log(update: Update, context: CallbackContext):
    file = open('logs.log', 'a')
    file.write(f'{dt.datetime.today().replace(microsecond=0)}:\
                {update.effective_user.first_name}:\
            {update.effective_user.id}:\
        {update.message.text}\n')
    file.close()