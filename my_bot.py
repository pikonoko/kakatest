import telebot
bot = telebot.TeleBot('8415264733:AAE5td5dgQBLsFSH3OUqNxCadPl9BKvd8QQ')
@bot.message_handler(commands=['KAKAGO'])
def KAKAGO(message):
    bot.send_message(message.chat.id, 'HELLO MY KAKULIACHKA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'the procces has started now u can kaka')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, '/start\n/KAKAGO\n/info\n/random\n/datekaka\n/timekaka')
from random import choice, randint
@bot.message_handler(commands=['random'])
def random(message):
    a = ['ti segodnia ne pokakaeshi','ti segodnia obosreshsia','tvoi drug obosretsia', 'vse okey']
    bot.send_message(message.chat.id, f'{choice(a)}')
from datetime import datetime, date
a = datetime.now()
@bot.message_handler(commands=['datekaka'])
def datekaka(message):
    b = a.strftime('%m month %d day')
    bot.send_message(message.chat.id, f'now is:\n{b}')

@bot.message_handler(commands=['timekaka'])
def datekaka(message):
    b = a.strftime('%H:%M')
    bot.send_message(message.chat.id, f'now is:\n{b}')

@bot.message_handler(commands=['bye'])
def bye(message):
    bot.send_message(message.chat.id, "Byee my friend!!" )


bot.polling(none_stop=True)



