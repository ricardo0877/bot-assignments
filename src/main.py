import assignments
import telebot

bot = telebot.TeleBot("1545886121:AAEFlARQil0-PBAjxPzR5iVWSHUhOVlDcgo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	assignments_msg = assignments.get_assignments()
	chat_id = -585783047

	if len(assignments_msg) > 4096:
		splitted_msg = telebot.util.split_string(assignments_msg, 3000)
		for text in splitted_msg:
			bot.send_message(chat_id, text)
	else:
		bot.send_message(chat_id, text)

bot.polling()