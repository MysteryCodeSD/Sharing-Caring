import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5026196758:AAEfM8mXy_fJyg428cVmtgaykClD_6tBZvo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "6878048"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3833ae3a7415af46df46a83a3ba2c432")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001591341300"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1789263079"))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "postgres://hfpugmctfcnbzn:52ea7db32c8c80390994000c773434cd4f963f54e6ace631215f495956756f42@ec2-54-75-246-118.eu-west-1.compute.amazonaws.com:5432/d22f9j44ho3cj9")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001537223060"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<i>Nice to Meet You {mention}</i> \n\n⚡𝑰 𝒂𝒎 𝑴𝒐𝒔𝒕 𝑽𝒆𝒓𝒔𝒂𝒕𝒊𝒍𝒆 𝑭𝒊𝒍𝒆 𝑺𝒕𝒐𝒓𝒆 𝑩𝒐𝒕 𝑶𝒇 𝑭𝒖𝒁𝒊𝒐𝒏𝑿. \n\n⚡Mᴀᴅᴇ Wɪᴛʜ Pʏᴛʜᴏɴ3 Wɪᴛʜ ❤️⚡ \n\n<i>⚡️𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 :  @FuZionX</i>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1841065457 1822295565 692234972 1242011540").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>{previouscaption}</b> \n\n<i>⚡️𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 :  @FuZionX⚡</i>")

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
