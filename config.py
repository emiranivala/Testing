# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22642292"))
API_HASH = getenv("API_HASH", "4502d35191a2fcb02c8467f54789f0ea")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "922270982").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002230414810")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002304203111"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "20"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", None)
AD_API = getenv("AD_API", None)
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
