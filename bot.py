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
import requests
import json
import time

# Logging and Bot config
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


updater = Updater("5065508658:AAHP9MQjkJ-HGGoExsoQ4z6oN4EYL1xxwsw",
                  use_context=True)

# Global Variables
Address = "Address not set"
coin = "USD"

def help(update: Update, context: CallbackContext):
    update.message.reply_text("Use /start to start the bot")

def start(update: Update, context: CallbackContext):

    keyboard = [
        [
            InlineKeyboardButton("⚙️Settings", callback_data='settings'),
            InlineKeyboardButton("▶️Start", callback_data='StartRequestData'),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=reply_markup, text="Welcome to the Moneroocean Bot")


def reply(update, context):
    user_input = update.message.text
    update.message.reply_text(ReturnAddress(user_input, update, context))

def ReturnAddress(user_input, update, context):
    keyboard = [
        [
            InlineKeyboardButton("↩️Back", callback_data='settings'),
        ],
    ]

    global Address
    Address = user_input
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=reply_markup, text="Your address has been changed to " + Address)


def queryHandler(update: Update, context: CallbackContext):
    global Address
    query = update.callback_query.data
    update.callback_query.answer()

    if "StartRequestData" in query:
        # Variables:
        url = f'https://api.moneroocean.stream/miner/{Address}/stats/'
        url_payments = f'https://api.moneroocean.stream/miner/{Address}/payments'
        url_MoneroPrice = 'https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=BTC,USD,EUR,RUB'
        # JSON commands
        r = requests.get(url)
        price = requests
        stats_json = r.json()
        stats_str = json.dumps(stats_json)

        # Hashrate
        Hashes = int(stats_json["hash2"])
        KiloHashesRAW = Hashes/1000
        KiloHashes = round(KiloHashesRAW)
        KHsText = str(KiloHashes) + " KH/s"

        # Amount Due
        rawAmtDue = (stats_json["amtDue"])
        amtDue = rawAmtDue * 10**-12
        amtDueRounded = round(amtDue, 6)
        amtDueText = str(amtDueRounded) + " XMR"

        # Amount Paid
        rawAmtPaid = (stats_json["amtPaid"])
        amtPaid = rawAmtPaid * 10**-12
        amtPaidRounded = round(amtPaid, 6)
        amtPaidText = str(amtPaidRounded) + " XMR"

        text = "These are your current Statistics:\n\nYour total hashrate is: " + KHsText + "\nYour total due amount is:\n" + amtDueText + "\nYour total paid amount is:\n" + amtPaidText

        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    if "settings" in query:

        keyboard = [
            [
                InlineKeyboardButton("❌Delete address", callback_data='DelAddress'),
                InlineKeyboardButton("✅Add address", callback_data='AddAddress'),

            ],
            [
            InlineKeyboardButton("↩️Back", callback_data='BackStart'),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, text="The currently set address is: " + Address, reply_markup=reply_markup)

    if "BackStart" in query:
            keyboard = [
                [
                    InlineKeyboardButton("⚙️Settings", callback_data='settings'),
                    InlineKeyboardButton("▶️Start", callback_data='StartRequestData'),
                ],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=reply_markup, text="Welcome to the Moneroocean Bot")


    if "DelAddress" in query:
        keyboard = [
            [
                InlineKeyboardButton("↩️Back", callback_data='settings'),
                ],
                ]

        Address = "No address set"
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=reply_markup, text="Your address has been deleted")


    if "AddAddress" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter your wallet address")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
updater.dispatcher.add_handler(CallbackQueryHandler(queryHandler))
updater.start_polling()
