import telebot

TOKEN = '5790395281:AAG1nkwrvqeJWmcvmIjgNNVDIBjHWRB1Wvo'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_answer(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f'Вы прислали команду: {msg.text}')


# @bot.message_handler()
# def answer(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text=f'Вы прислали: {msg.text}')

import random


left = 100
current_player = random.randint(0, 1)
@bot.message_handler()
def answer(msg: telebot.types.Message):
    global left, current_player
    if current_player == 1:
        bot.send_message(chat_id=msg.from_user.id, text='Ход бота')
       
    else:
        bot.send_message(chat_id=msg.from_user.id, text='Ход пользователя')
        
    amount = bot_move(left) if current_player == 1 else player_move(left, msg.text)
    
    
    if not amount:
        bot.send_message(chat_id=msg.from_user.id, text='Введи снова')
        return
    
    bot.send_message(chat_id=msg.from_user.id, text=f'Взято конфет: {amount}')
    left -= amount
    
    bot.send_message(chat_id=msg.from_user.id, text=f'Осталось на столе конфет: {left}')
    if left == 0:
        bot.send_message(chat_id=msg.from_user.id, text='Игра окончена')
        left = 100
        
    current_player = (current_player + 1) % 2


def player_move(left, amount):
    if not amount.isnumeric():
        return 0
    amount = int(amount)
    if amount <= 0 or amount >= 29:
        return 0
    if amount > left:
        return 0
    return amount


def bot_move(left):
    if left <= 57 and left > 29:
        amount = left - 29
        return amount
    elif left < 29:
        amount = left
        return amount
    else:
        amount = random.randint(1, 28)
        return amount



bot.polling()