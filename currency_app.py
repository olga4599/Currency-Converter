import telebot
from currency_token import TOKEN, keys
from extensions import CryptoConverter, APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = '<Enter currency name: > <From Currency: > <To Currency: > <Amount: > \n ' \
           'Available currency: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currency: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException("Too many parameters")

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'User error. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Command cannot be fulfilled')
    else:
        text = f'Price {amount} {quote} in {base} - {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling()