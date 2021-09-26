if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1955901827:AAHglsK-oCFxGKGPlgq4gmO91ThEK5jDwp0"
    OWNER_ID = "1179081526" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "justchillin27"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 
    'postgres://wvufrieyvmdsso:5bf748da5a5cddc8cf7cc1601dae9c52865495e911bb320873a33d5d507b2c2d@ec2-34-197-135-44.compute-1.amazonaws.com:5432/derooqjcl0mj1v'
  # needed for any database modules, 
    #postgresql://postgres:postgres@localhost:5432/rose_sc_clone'
    MESSAGE_DUMP = "-1001421186460"  # needed to make sure 'save from' messages persist
    USE_MESSAGE_DUMP = True
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
