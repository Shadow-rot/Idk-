# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/TeamX/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    ANILIST_CLIENT = "8679"
    ANILIST_SECRET = "NeCEq9A1hVnjsjZlTZyNvqK11krQ4HtSliaM7rTN"
    API_ID = 19733238  # integer value, dont use ""
    API_HASH = "fe955e75a36ec386ae9ded33061fbd98"
    BOT_TOKEN = "6057458299:AAGpnzKWjcQ0MUNu5KRwMeSKJjnCfL3l7tI"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5148561602  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Aceadi"
    SUPPORT_CHAT = "NexusXsupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001504105950
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001504105950
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ERROR_LOGS = (
        -1001733372611
    )  # Prints information Error

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://pnnikbfp:T6PvVZVtMe1AG2h-7CwngQILR-M2y1FF@snuffleupagus.db.elephantsql.com/pnnikbfp"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "3624487efd8e4ca9c949f1ab99654ad1e4de854f41a14afd00f3ca82d808dc8c"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    STRICT_GMUTE = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "-V48U2FLLKRHSVD4X"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "-1CUBX1HXGNHW"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "2455acab48f3a935a8e703e54e26d121"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = "xYCR1ZyK3ZsofjH7Y6hPcyzC"
    OPENWEATHERMAP_ID = "887da2c60d9f13fe78b0f9d0c5cbaade"
    TRIGGERS = "/ !"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
