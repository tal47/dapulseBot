# dapulseBot

Welcome to dapulseBot! I am a baic python Telegram bot that allows you to send pulses into a desired board in Dapulse.

### How to run your bot

  - First, [create a bot through the BotFather] on Telegram.
  - You sould have your api_key from your Dapulse UI (Admin -> API), Telegram bot token from BotFather, and board id (you can get it from it's URL on Dapulse UI).

### Commandline

```sh
$ git clone https://github.com/tal47/dapulseBot.git
$ cd dapulseBot
$ dapulseBot.py <api_key> <token> <room_id>
```

##### For example

```sh
$ dapulseBot.py 6b25fg4y523a355y4hb13 123456789:ABcDefGuliujndWivkapwAAA 143256789
```

#### TODO
 - Docker

   [create a bot through the BotFather]: https://github.com/python-telegram-bot/python-telegram-bot
