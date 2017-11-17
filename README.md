# Versup
Versup bot is a [Telegram](https://telegram.org) bot which follows Android app versioning. This one can be really useful if you want to reverse-engineer one or few well-known Android apps.
Thanks to a polling mechanism, the bot will periodically check via the Google Play API if a new version is available. If so, the new APK will be store into a local directory and you will be notified with a Telegram message.
Obviously, you're free to choose the followed app(s).

# Requirements

First of all, you have to install Python 2.7, PyPi and Git. 
In the following guide, I will assume that you're on a Debian-based operating system. If it's currently not your case, I think [DuckDuckGo](https://duckduckgo.com/) or [Google](https://www.google.co.uk/) are willing to help you. 

To do so, just run this command:
```
apt update && apt install python python-pip git
```

# Installation

To install the dependencies, you have to run this command:
```
pip install -r requirements.txt
```

# Usage

## Getting started

Initially, you have to get a bot token. You can obtain one by talking with @BotFather (more information [here](https://core.telegram.org/bots#6-botfather)).
Then, you must have a Google account in order to access Google Play. I highly advise you to create a dedicated one with a random password that you won't use anywhere.

Now, with this information, you're able to properly fill the file "config.json", which is located in the root of the project.  

This file must contains the following values:
  + emailAddress
    > Your Google email address
  + password
    > Your Google password
  + botToken
    > Your Telegram bot token
  + refreshRate
    > Number of minute(s) between each version checking (default: 30). Note that you will probably be banned from Google services if you set a low value.

Finally, you have to run this command in order to launch the bot:
```
python versup.py
```
If you haven't any error in the output log, your bot is able to receive new commands via Telegram.

## Commands
Thanks to these available commands, you will be able to communicate with your Versup bot:
  + /start
    > Initialize the bot.
  + /ping
    > Ping the bot (in order to see if he's up for example).
  + /status
    > Get the current status of the bot.
  + /version [appId]
    > Get the current version of a given app. This command must be followed by an app ID.
  + /follow [appId]
    > Follow a specified app. This command must be followed by an app ID.
  + /unfollow [appId]
    > Unfollow an app. This command must be followed by an app ID.

## How to find an app ID?

The easiest way to do so is to access [Google Play](https://play.google.com/store) with your favorite web browser and just search your targeted app.
You should find the app ID in the URL in the HTTP GET parameter called "id".
For instance, the app ID of Snapchat is "com.snapchat.android".

# License

Versup is licensed under the GNU GPL license. Have a look at the [LICENSE](https://github.com/bla5r/Versup/blob/master/LICENSE) for more information.

# Credits

  + [python-telegram-bot](https://github.com/python-telegram-bot): All Telegram interactions are based on the project [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
  + [NoMore201](https://github.com/NoMore201): All Google Play interactions are based on the project [googleplay-api](https://github.com/NoMore201/googleplay-api)

# Contact

If you have any question about the project, feel free to contact me on Twitter: [@bla5r](https://twitter.com/bla5r) 
