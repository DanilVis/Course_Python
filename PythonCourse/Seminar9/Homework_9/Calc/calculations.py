from telegram import Update
from telegram.ext import ContextTypes
from calc_op import calc_sum, calc_div, calc_mult, calc_sub, calc_exponent
from calc_logging import write_log, op_log


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    write_log(update, context)
    expression = update.message.text[6:] if len(update.message.text) > 6 else ""
    a, op, b = expression.split()
    a = number_check(a)
    b = number_check(b)
    if not a or not b:
        await update.message.reply_text("Неверный ввод! Попробуйте ещё раз.")
        return
    if op == "+":
        res = calc_sum(a, b)
    elif op == "-":
        res = calc_sub(a, b)
    elif op == "*":
        res = calc_mult(a, b)
    elif op == ":" or op == "/": 
        res = calc_div(a, b)
    elif op == "**" or op == "^":
        res = calc_exponent(a, b)
    else:
        await update.message.reply_text("Неверный ввод! Попробуйте ещё раз.")
        return
    op_log(update, context, res)
    await update.message.reply_text(str(res)) # преобразуется в строку, так как в случае комплексного числа выдает ошибку
    


def number_check(num):
    try: 
        return float(num)
    except: 
        try:
            return complex(num)
        except: 
            return ""
