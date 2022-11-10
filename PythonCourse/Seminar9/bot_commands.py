from telegram import Update
from telegram.ext import ContextTypes
import datetime
from spy import *
import random

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/sum\n/help')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text  # ~input
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')  # ~print


async def w_d_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    input_text = update.message.text[4:] if len(update.message.text) > 4 else ""
    input_text = words_delete(input_text)
    if input_text:
        await update.message.reply_text(input_text)


async def rand_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    input_text = update.message.text[5:] if len(update.message.text) > 5 else ""
    randomlist = input_text.split() if input_text else []
    if not input_text:
        randomlist = random.sample(range(10), 5)
    await update.message.reply_text(randomlist)
    random.shuffle(randomlist)
    await update.message.reply_text(randomlist)


def words_delete(input_text):
    if not input_text:
        return ""
    input_text = list(filter(lambda x: 'абв' not in x, input_text.split()))
    return " ".join(input_text)
