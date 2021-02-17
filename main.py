import telebot
from config import token, keyboard_main
import currency
from telebot import types

bot = telebot.TeleBot(token)
index_option = 'buy'
currency_calculate_type =  'USD'

@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    for value in keyboard_main.values():
        keyboard.add(value)
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}! Select your option!)', reply_markup=keyboard)

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
        markup_inline = show_currency_option()

        bot.send_message(message.chat.id, f'{message.from_user.first_name}, select your currency:', reply_markup=markup_inline)
        


@bot.callback_query_handler(func = lambda call: True)
def select_currency(call):
    global currency_calculate_type
    global index_option

    if call.data == 'usd_click':
        bot.send_message(call.message.chat.id , currency.get_usd_currency())
    elif call.data == 'eur_click':
        bot.send_message(call.message.chat.id, currency.get_eur_currency())
    elif call.data == 'rur_click':
        bot.send_message(call.message.chat.id, currency.get_rur_currency())
    elif call.data == 'btc_click':
        bot.send_message(call.message.chat.id, currency.get_btc_currency())
    elif call.data == 'usd_calculate':
        currency_calculate_type = 'USD'

        bot.send_message(call.message.chat.id, f'Your currency is {currency_calculate_type}. Select your operation: ', reply_markup=show_operation())
    elif call.data == 'eur_calculate':
        currency_calculate_type = 'EUR'

        bot.send_message(call.message.chat.id, f'Your currency is {currency_calculate_type}. Select your operation: ', reply_markup=show_operation())
    elif call.data == 'rur_calculate':
        currency_calculate_type = 'RUR'

        bot.send_message(call.message.chat.id, f'Your currency is {currency_calculate_type}. Select your operation: ', reply_markup=show_operation())
    elif call.data == 'btc_calculate':
        currency_calculate_type = 'BTC'

        bot.send_message(call.message.chat.id, f'Your currency is {currency_calculate_type}. Select your operation: ', reply_markup=show_operation())

    elif call.data == 'buy_calculate':
        index_option = 'buy'

        msg = bot.send_message(call.message.chat.id, 'Enter number money in format "100.00"')
        bot.register_next_step_handler(msg, calculate)

    elif call.data == 'sell_calculate':
        index_option = 'sell'

        msg = bot.send_message(call.message.chat.id, 'Enter number money in format "100.00"')
        bot.register_next_step_handler(msg, calculate)


def calculate(message):
    global index_option
    global currency_calculate_type

    try:
        number = eval(message.text)
        result = round(currency.calculate(number, index_option, currency_calculate_type), 2)
        print(result)
        bot.send_message(message.chat.id, str(result))

    except Exception as ex:
        print(ex)
        msg = bot.send_message(message.chat.id, "Your enter's value must be in format \"100\" or \"100.00\"")
        bot.register_next_step_handler(msg, calculate)

        
def show_operation():
    markup = types.InlineKeyboardMarkup()

    buy_btn = types.InlineKeyboardButton(text= 'Buy', callback_data='buy_calculate')
    sell_btn = types.InlineKeyboardButton(text = 'Sell', callback_data='sell_calculate')

    markup.add(buy_btn, sell_btn)
    return markup

def show_currency_option():
    markup_inline = types.InlineKeyboardMarkup()

    usd_btn = types.InlineKeyboardButton(text = 'UAH - USD', callback_data='usd_calculate')
    eur_btn = types.InlineKeyboardButton(text = 'UAH - EUR', callback_data='eur_calculate')
    rur_btn = types.InlineKeyboardButton(text = 'UAH - RUR', callback_data='rur_calculate')
    btc_btn = types.InlineKeyboardButton(text = 'USD - BTC', callback_data='btc_calculate')

    markup_inline.add(usd_btn, eur_btn, rur_btn, btc_btn)
    return(markup_inline)
    



if __name__=='__main__':
    bot.polling(none_stop = True, interval= 0)
