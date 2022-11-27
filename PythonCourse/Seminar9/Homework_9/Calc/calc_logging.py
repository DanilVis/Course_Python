from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime


FILE_NAME = "calc_log.csv"


def write_log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open(FILE_NAME, 'a', encoding='UTF-8')
    file.write(f'{datetime.now().strftime("%d.%m.%Y %H:%M")}, {update.effective_user.first_name}, '
    f'{update.effective_user.id}, {update.message.text}\n')
    file.close()


def op_log(update: Update, context: ContextTypes.DEFAULT_TYPE, text):
    file = open('results_log.csv', 'a', encoding='UTF-8')
    file.write(f'{update.message.text[6:]} = {text}\n')
    file.close()

async def show_log_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('results_log.csv', 'r', encoding='UTF-8')
    log = file.read().strip().split('\n')
    if log == ['']:
        await update.message.reply_text('Журнал вычислений пустой')
    else: 
        if len(log) > 5:
            log = log[-5:]
        await update.message.reply_text("\n".join(log))
    file.close()
