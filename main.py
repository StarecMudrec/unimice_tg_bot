import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=['ping'])
def ping(message):
  bot.reply_to(message, "Pong!")

@bot.message_handler(commands=['help'])
def help(message):
  bot.reply_to(message, "This bot has ping and help commands.")

bot.polling()