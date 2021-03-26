import assignments
import telebot

bot = telebot.TeleBot("1545886121:AAEFlARQil0-PBAjxPzR5iVWSHUhOVlDcgo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	assignments_msg = assignments.get_assignments()

	if len(assignments_msg) > 4096:
	    for x in range(0, len(assignments_msg), 4096):
	        bot.reply_to(message, assignments_msg[x:x+4096])
	else:
		bot.reply_to(message, assignments_msg)

bot.polling()