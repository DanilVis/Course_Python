from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from calculations import calc_command
from menu import start_command, help_command
from calc_logging import show_log_command


app = ApplicationBuilder().token("YOUR_TOKEN").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("log", show_log_command))
print('server start')

app.run_polling()
