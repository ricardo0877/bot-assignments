import assignments_filter
import telebot

bot = telebot.TeleBot("1545886121:AAEFlARQil0-PBAjxPzR5iVWSHUhOVlDcgo", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['tarefas'])
def send_welcome(message):
	bot.reply_to(message, assignments_filter.get_assignments())

bot.polling()