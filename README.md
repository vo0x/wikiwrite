# Telegram Bot

This is a Telegram bot built using the Python Telegram Bot (PTB) library. 

## Features
- **search:** on wikipedia.
- **translate** with the trengine by @z44d.
- **sqlite db** /brodcast <message> for send message to the users, /stats to get the bot stats.

## Requirements
- Python 3.7+
- Python-telegram-bot
- wikipedia
- trengine 

## Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/vo0x/wikiwrite.git
    cd bot
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. replace  your bot_token and owner_id :
    ```python
    # config.py

    bot_token = "your-telegram-bot-token"
    owner = 123456789  # Replace with your Telegram ID
    ```

4. Run the bot:
    ```bash
    python3 bot.py
    ```


