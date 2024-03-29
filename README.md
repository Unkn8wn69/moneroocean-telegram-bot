# Moneroocean Telegram Bot
#### by u/unkn8wn69

The Moneroocean Telegram Bot is a tool to request the statistic of the users specified monero address.
The Project is in early development and can't considered a full version yet

## Preview

<img src="Preview.png">  


## Features

* Set an Address
* Request Hashrate, Amount Due and Amount Paid from the Moneroocean API of your set address.
* Amounts shown in your preferred currency
* Get profit forecasts for daily, weekly, monthly and yearly profits in your selected currency

## Upcoming Features

* Better UI and text content of messages
* Automatic sending of statistical data in a period of time that is specified by the User
* Multiple addresses
* Payment history 
* Payout threshold settings
* fixedfloat.com crypto convert API

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
3. Save the file and execute it with python-3.9.9
```
$ python bot.py
```
Make sure you install the python-telegram-bot library with ```$ pip install python-telegram-bot```

### 

## Author

* **Unkn8wn69**
* Credit to **Moneroocean** 


## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](/LICENSE) file for details

## Donate

Monero(XMR): ```493e1fciPXh1ZBnUtDan7QZKmnNGzQyCMU2U7MCg1mxyWyiaHKyBKxS7sZsg5uA9mZZyshw54dwHxAVDNsULfXTv4GEHUWo```

BTC:        
https://fixedfloat.com/exchange/btc-to-xmr

LTC:          
https://fixedfloat.com/exchange/ltc-to-xmr

ETH:           
https://fixedfloat.com/exchange/eth-to-xmr
