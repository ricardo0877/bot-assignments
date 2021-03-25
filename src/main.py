import assignments
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='1545886121:AAEFlARQil0-PBAjxPzR5iVWSHUhOVlDcgo', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=(for x in assignments.get_assignments()))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()