from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import math
import cmath
from spy import *


def check_number(item):
    try:
        if item[-1] == 'j': item = complex(item)
        else:
            item = float(item)
            if item % 1 == 0: item = int(item)
    except ValueError:
        return False
    return item


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Bot commands:\n'\
                                    '/hello - greeting the bot\n'\
                                    '/help - avaliable commands\n'\
                                    '/calc - calculate two numbers:\n'\
                                    '   + : sum\n'\
                                    '   - : subtract\n'\
                                    '   * : multiply\n'\
                                    '   / : divide\n'\
                                    '   ** : pow\n')

async def calculator_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    num_1 = check_number(items[1])
    math_sign = items[2]
    num_2 = check_number(items[3])
    if (num_1 == False) or (num_2 == False):
        await update.message.reply_text('Incorect math expression.')
    else:
        if math_sign == '+':
            await update.message.reply_text(f'{num_1} + {num_2} = {num_1 + num_2}')
        if math_sign == '-':
            await update.message.reply_text(f'{num_1} - {num_2} = {num_1 - num_2}')
        if math_sign == '*':
            await update.message.reply_text(f'{num_1} * {num_2} = {num_1 * num_2}')
        if math_sign == '/':
            await update.message.reply_text(f'{num_1} / {num_2} = {num_1 / num_2}')
        if math_sign == '**':
            await update.message.reply_text(f'{num_1} ** {num_2} = {pow(num_1, num_2)}')
        if (math_sign != '+') and (math_sign != '-') and (math_sign != '/') and (math_sign != '*') and (math_sign != '**'):
            await update.message.reply_text('Unknown operation.')

'''
async def phone_directory(update: Update, context: CallbackContext) -> None:

    phoneDirectoryPath = StartProgram()

    while phoneDirectoryPath == '':
        phoneDirectoryPath = FirstActionSelect()

    if phoneDirectoryPath != 0:
        action = 0
        while action < 5:
            action = ActionSelect(phoneDirectoryPath)
    else:
        await update.message.reply_text(f'Phone directoty is closed, {update.effective_user.first_name}')
'''