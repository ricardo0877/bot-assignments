import assignments
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging. )

updater = Updater(token='1545886121:AAEFlARQil0-PBAjxPzR5iVWSHUhOVlDcgo', use_context=True)
dispatcher = updater.dispatcher

def start(updater, context):
	message = assignments.get_assignments()
	if len(message) > 4096: 
		for x in range(0, len(message), 4096): 
			updater.send_message(updater.effective_chat.id, message[x:x+4096]) 
	else: 
		updater.send_message(updater.effective_chat.id, message)

	context.updater.send_message(chat_id=updater.effective_chat.id, text=message)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()