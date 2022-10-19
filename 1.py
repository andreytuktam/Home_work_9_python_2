# Напишите бота, удаляющего из текста все слова, содержащие "абв". (текст вводит пользователь)

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5790395281:AAG1nkwrvqeJWmcvmIjgNNVDIBjHWRB1Wvo')
updater = Updater(token='5790395281:AAG1nkwrvqeJWmcvmIjgNNVDIBjHWRB1Wvo')
dispatcher = updater.dispatcher


def message(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, f'{" ".join(filter(lambda x: "абв" not in x, text.split()))}\n Вот :)')


message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()  