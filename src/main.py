import assignments
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='1545886121:AAEFlARQil0-PBAjxPzR5iVWSHUhOVlDcgo', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
	message = assignments.get_assignments()
	context.bot.send_message(chat_id=update.effective_chat.id, text=message[0])

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()