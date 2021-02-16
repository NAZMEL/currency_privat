import telebot
from config import token, keyboard_main
import currency
from telebot import types

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    for value in keyboard_main.values():
        keyboard.add(value)
    bot.send_message(message.chat.id, 'Hi! Select your option!)', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def click_exchange_rate(message):
    if  message.text == keyboard_main['currency_rate'] :
        text = currency.get_all_currency()
        bot.send_message(message.chat.id, text)

    elif message.text == keyboard_main['select_currency']:
        markup_inline = types.InlineKeyboardMarkup()

        usd_button = types.InlineKeyboardButton(text = 'USD', callback_data='usd_click')
        eur_button = types.InlineKeyboardButton(text = 'EUR', callback_data='eur_click')
        rur_button = types.InlineKeyboardButton(text = 'RUR', callback_data='rur_click')
        btc_button = types.InlineKeyboardButton(text = 'BTC', callback_data='btc_click')

        markup_inline.add(usd_button, eur_button, rur_button, btc_button)

        bot.send_message(message.chat.id, 'Select currency: ', reply_markup= markup_inline)

    elif message.text == keyboard_main['calculator']:
        bot.send_message(message.chat.id, '😃 jdkgjksdl')


@bot.callback_query_handler(func = lambda call: True)
def select_currency(call):
    if call.data == 'usd_click':
        bot.send_message(call.message.chat.id , currency.get_usd_currency())
    elif call.data == 'eur_click':
        bot.send_message(call.message.chat.id, currency.get_eur_currency())
    elif call.data == 'rur_click':
        bot.send_message(call.message.chat.id, currency.get_rur_currency())
    elif call.data == 'btc_click':
        bot.send_message(call.message.chat.id, currency.get_btc_currency())
    



if __name__=='__main__':
    bot.polling(none_stop = True, interval= 0)
