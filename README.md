# Telegram-Bot-Collection

This projects aims to make [Telegram](https://telegram.org) bots that will automate several small functions.

Current Bots:
- Tag anonymous admin in chat:
    When someone tags @admin, the bot will forward the message to one of them admins specified.

## Credits

This is based on:
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

## How do I run this?

**This code is tested on python 3.8.5**

1. Install Anaconda or Miniconda or Virtualenv
2. Install required modules shown requirements.txt
3. Change config.py with the required keys.
4. Run the bot of your choice `python <bot-name>.py`

## API Keys

You'll need a Telegram Bot Token, you can get it via BotFather ([more info here](https://core.telegram.org/bots)).
Then change the config.py file with your required ids.

**Getting your user id:**
1. Send a message to the bot.
2. Get the list of updates for your BOT:
    `https://api.telegram.org/bot<YourBOTToken>/getUpdates`
3. Look for the "message" object in the response and copy the id that matched your username.

**Getting your group id:**
1. Add the Telegram BOT to the group and send a random message to the group.
2. Get the list of updates for your BOT:
    `https://api.telegram.org/bot<YourBOTToken>/getUpdates`
3. Look for the "chat" object in the response and copy the id.

## TO-DO

- Improve logging
- Increase capacity
- Create more bots