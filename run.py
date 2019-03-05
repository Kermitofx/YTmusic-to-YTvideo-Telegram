import logging
import os

from telegram import MessageEntity
from telegram.ext import Updater, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
FIND = 'music.youtube.com'
REPLACE = 'youtube.com'


def parse_url(update, context):
    text = update.message.text
    if FIND not in text:
        return

    response = text.replace(FIND, REPLACE)
    update.message.reply_text(response)


if __name__ == '__main__':
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    echo_handler = MessageHandler(
        Filters.text & (Filters.entity(MessageEntity.URL) | Filters.entity(MessageEntity.TEXT_LINK)),
        parse_url
    )
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()
    updater.stop()
