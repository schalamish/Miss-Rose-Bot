from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1179081526  # my telegram ID
    OWNER_USERNAME = "justchillin27"  # my telegram username
    API_KEY = "1955901827:AAHglsK-oCFxGKGPlgq4gmO91ThEK5jDwp0"  # my api key, as provided by the botfather
   
    SQLACHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/rose_sc_clone'  #sample db credentials
    MESSAGE_DUMP = '-1001421186460' #some group chat that your bot is a member of
    
 
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

 
