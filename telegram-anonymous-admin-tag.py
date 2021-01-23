# telegram-anonymous-admin-tag.py
# Uses telegram_bot_token, group_chat_id, admin_chat_id
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import logging
import os
from config import telegram_bot_token, group_chat_id, admin_chat_id

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, but i do not have any other commands.")


def checkReplyToAdmin(update, context):
    message_text = update.message.text

    if "@admin" in message_text: 
        context.bot.forward_message(chat_id=admin_chat_id, from_chat_id=update.message.chat_id,
                        message_id=update.message.message_id)


checkReplyToAdmin_handler = MessageHandler(Filters.text & (~Filters.command) & Filters.chat(group_chat_id), callback=checkReplyToAdmin)
dispatcher.add_handler(checkReplyToAdmin_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()