import telebot
import constants
from telebot import types
from news_stack import NewsStack
from buttons_manager import ButtonsManager


token = open('token').read()
bot = telebot.TeleBot(token)


def actions_markup():
    markup = types.InlineKeyboardMarkup()
    seeNews = button_manager.getSeeNewsButton()
    ejectNews = button_manager.getEjectNewsButton()
    addNews = button_manager.getAddNewsButton()
    toBegin = button_manager.getToBeginButton()

    seeNews and markup.add(seeNews)
    ejectNews and markup.add(ejectNews)
    addNews and markup.add(addNews)
    toBegin and markup.add(toBegin)

    return markup


@bot.message_handler(regexp=".*")
def any_message(message):
    news_stack.last_message = message.text
    markup = actions_markup()

    bot.send_message(message.chat.id, constants.MENU_TEXT, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    chat = call.message.chat
    answer_text = constants.CMD_NOT_FOUND

    if call.data == constants.SEE_CMD:
        bot.send_message(chat.id, news_stack.see())
        answer_text = constants.SEE_RES_TEXT
    elif call.data == constants.EJECT_CMD:
        bot.send_message(chat.id, news_stack.eject())
        answer_text = constants.EJECT_RES_TEXT
    elif call.data == constants.ADD_CMD:
        news_stack.add_last_message()
        answer_text = constants.ADD_RES_TEXT
    elif call.data == constants.TO_BEGIN_CMD:
        news_stack.pt = 0
        answer_text = constants.TO_BEGIN_RES_TEXT

    markup = actions_markup()

    bot.send_message(call.message.chat.id, answer_text, reply_markup=markup)
    bot.answer_callback_query(call.id)


if __name__ == '__main__':
    news_stack = NewsStack()
    button_manager = ButtonsManager(news_stack)

    bot.polling()
