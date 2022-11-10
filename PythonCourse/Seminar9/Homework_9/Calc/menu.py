from telegram import Update
from telegram.ext import ContextTypes
from calc_logging import write_log


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    write_log(update, context)
    await update.message.reply_text(f'Здравствуйте, {update.effective_user.first_name}! '
    'Вас приветствует телеграм-калькулятор. '
    'Начните вычисления или отправьте /help, чтобы узнать о работе калькулятора.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    write_log(update, context)
    await update.message.reply_text(f'Калькулятор работает с рациональными числами '
    'и комплексными числами вида 2+3j.\n /start - начать работу\n /help - вызов '
    'подсказки\n /calc - сделать вычисления\n Введите команду и выражение из двух '
    'чисел с одним из символов операций: +, -, *, /.')
