import configparser
import os

import telegram


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(CURRENT_DIR), 'config.ini'))
api_token = config['TELEGRAM']['API_TOKEN']


def telegram_bot(message):
    bot = telegram.Bot(token=api_token)
    chat_id = bot.getUpdates()[-1].message.chat.id
    bot.sendMessage(chat_id=chat_id, text=message)
    return bot
