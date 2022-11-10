from telegram import Update
from telegram.ext import ContextTypes


FILE_NAME = "calc_log.csv"


def write_log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open(FILE_NAME, 'a', encoding='UTF-8')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()
