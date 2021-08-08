#Soon Launching Combined Repo


import os

class Config(object):
    # get it from my.telegram.org
    APP_ID = os.environ.get("APP_ID", "3546656")
    API_HASH = os.environ.get("API_HASH", "48b79c54af688f05c350161bddea414c")
    # Get it from @botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1728730929:AAESo9G0f62qLCXJnOWcKzp5Vblmrktivd4")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "PATRICIA_ROBOT")
    # Leave this defualt
    SESSION_NAME = os.environ.get("SESSION_NAME", "JV_CaptchaBot")
    # get it from https://cloud.mongodb.com 
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Evil:NRb0LXgSBdao6tHB@cluster0.phtr6.mongodb.net/EvilretryWrites=true&w=majority")
    # Ask in https://t.me/JV_Community
    API_TOKEN = os.environ.get("API_TOKEN", "dontsellme_iamfreeapi")
    # Sudo users(goto @JVToolsBot and send /id to get your id)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1204927413 1405957830").split()))
    SUDO_USERS.append(1204927413)
    SUDO_USERS = list(set(SUDO_USERS))
