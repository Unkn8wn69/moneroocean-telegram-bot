from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import *
from telegram.ext import *
from requests import *
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


updater = Updater("YOUR BOT KEY",
                  use_context=True)


global Address
Address = "No Address Set"

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Use /start to start the bot")

def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Settings", callback_data='settings'),
            InlineKeyboardButton("Start", callback_data='StartButton'),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=reply_markup, text="Welcome to the Moneroocean Bot")

def reply(update, context):
    user_input = update.message.text
    update.message.reply_text(ReturnAddress(user_input))

def ReturnAddress(user_input):
    Address = user_input
    answer = "Your address has been changed to " + Address
    return answer


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global Address

    if "settings" in query:
        keyboard = [
            [
                InlineKeyboardButton("Delete address", callback_data='DelAddress'),
                InlineKeyboardButton("Add address", callback_data='AddAddress'),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text="The currently set address is: " + Address, reply_markup=reply_markup)

    if "DelAddress" in query:
        Address = "No address set"

    if "AddAddress" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your Wallet Address")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
updater.dispatcher.add_handler(CallbackQueryHandler(queryHandler))
updater.start_polling()
