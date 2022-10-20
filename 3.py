import telebot

TOKEN = '5790395281:AAG1nkwrvqeJWmcvmIjgNNVDIBjHWRB1Wvo'

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start'])
# def start_answer(msg: telebot.types.Message):
#     bot.send_message(chat_id=msg.from_user.id, text=f'Вы прислали команду: {msg.text}')


@bot.message_handler()
def calculate(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text='''
    Выберите действие:
    + 
    - 
    * 
    / 
    ''')
    operation = str(msg.text)
    bot.send_message(chat_id=msg.from_user.id, text=operation)
    
    bot.send_message(chat_id=msg.from_user.id, text='''
    С какими числами будем работать:
    R - рациональные числа
    С - комплексные числа
    ''')
    choose = str(msg.text)
    bot.send_message(chat_id=msg.from_user.id, text=choose)
    
    if choose.upper() == 'R':
        
        
        bot.send_message(chat_id=msg.from_user.id, text='Введите первое число: ')
        number_1 = int(msg.text)
        bot.send_message(chat_id=msg.from_user.id, text='Введите второе число: ')
        number_2 = int(msg.text)
        if operation == '+':
            bot.send_message(chat_id=msg.from_user.id, text=('{} + {} = '.format(number_1, number_2)))
            bot.send_message(chat_id=msg.from_user.id, text=(number_1 + number_2))
        elif operation == '-':
            print('{} - {} = '.format(number_1, number_2))
            print(number_1 - number_2)
        elif operation == '*':
            print('{} * {} = '.format(number_1, number_2))
            print(number_1 * number_2)
        elif operation == '/':
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)
        else:
            print('Такой операции нет, попробуйте снова')
#             again()
#     if choose.upper() == 'C':
#         a_1 = int(input('Введите а1: '))
#         b_1 = int(input('Введите b1: '))
#         x = complex(a_1, b_1)
#         a_2 = int(input('Введите а2: '))
#         b_2 = int(input('Введите b2: '))
#         y = complex(a_2, b_2)
#         if operation == '+':
#             print('{} + {} = '.format(x, y))
#             print(x + y)
#         elif operation == '-':
#             print('{} - {} = '.format(x, y))
#             print(x - y)
#         elif operation == '*':
#             print('{} * {} = '.format(x, y))
#             print(x * y)
#         elif operation == '/':
#             print('{} / {} = '.format(x, y))
#             print(number_1 / number_2)
#         else:
#             print('Такой операции нет, попробуйте снова')
#             again()


# def again():
#     calc_again = input('''
#     Вам нужен калькулятор?
#     Введите Y если ДА или N если НЕТ.
#     ''')
#     if calc_again.upper() == 'Y':
#         calculate()
#     elif calc_again.upper() == 'N':
#         print('До встречи')
#     else:
#         again()
#         calculate()   
        


bot.polling()