# Moneroocean Telegram Bot
#### by u/unkn8wn69

The Moneroocean Telegram Bot is a tool to request the statistic of the users specified monero address.
The Project is in early development and can't considered a full version yet

## Features

* Set an Address
* Request Hashrate, Amount Due and Amount Paid from the Moneroocean API of your set address.

## Upcoming Features

* Better UI and text content of messages
* Automatic sending of statistical data in a period of time that is specified by the User
* Multiple addresses
* Payment history 
* Payout threshold settings

## Dependencies
> * python-3.9.9 & pip
> * python-telegram-bot pip package
> * Bot token by @BotFather on Telegram

## Installation

1. Clone or download the repository and navigate into it's downloaded folder 
```
$ git clone https://github.com/Unkn8wn69/moneroocean-telegram-bot/
$ cd moneroocean-telegram-bot
```
2. Edit the bot.py with your chosen file editor and paste in the bot token that you got handed when creating the bot at the @Botfather on telegram
```
updater = Updater("Telegram Bot API Key",
                  use_context=True)
```
3. Safe the file and execute it with python-3.9.9
```
$ python bot.py
```
Make sure you install the python-telegram-bot library with ```$ pip install python-telegram-bot```

### A publicly hosted instance of the bot is available under the username @moneroocean_en_bot
https://t.me/moneroocean_en_bot

## Donate

Monero(XMR): ```493e1fciPXh1ZBnUtDan7QZKmnNGzQyCMU2U7MCg1mxyWyiaHKyBKxS7sZsg5uA9mZZyshw54dwHxAVDNsULfXTv4GEHUWo```
</tr>
Bitcoin(BTC):
https://fixedfloat.com/exchange/btc-to-xmr
</tr>
Litecoin(LTC): 
https://fixedfloat.com/exchange/ltc-to-xmr
