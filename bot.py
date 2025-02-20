import telebot
from bot_logic import gen_pass # type: ignore
# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7870975205:AAHPWZJkvXudxqXZ1TkcgEf4cy5zifcgZ4I")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")
    

# Запускаем бота
bot.polling()