import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","20584104"))
API_HASH = getenv("API_HASH","f325ee578444d70ad2d02b0673f94d3a")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7164261117:AAFs8YEB0MIHpgXaNAeiAa8AgEgYrzEldnE")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kurt67143:DLArCT171SF9wRKJ@alexsoza.xpoqv.mongodb.net/?retryWrites=true&w=majority&appName=Alexsoza")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002065943011"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6387858072"))

# Fill Queue Limit . Example - 15
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "10"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/kumsalmuzsik/kumsalteam",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kumsaldestekkanal")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/GeceSohbettr")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", "BAE6FqgAs1u2wdl5Wu6m3wo2BVwFjnnAWjVN2MCdDI2XxJNN1WxIAbHE-lwdHjdolJUadvYpb9nE6sBTXJTZ0T_tNHieXx51PLwVcM65cRR9SQzB3KGXITSaS22gGiF2qwrdviYcoxfUPvWve1lkEtrjdwGO1H-fngv4bRT3KYq_rOi8pk8FfNYbHskX4SiLlAMT7ggz7tLb9kZ-8VHH9C25O9rwAtOWiC7pRgzHGJRiRWsdt8GjTnIMZsQqL8ICuwSC-1OTost_4D0hpYfu5mr9-V4RHIxoszTn2-GCym3RFIfQ3eeUEDcsu_jjI3uaI60-eSwWwZWlu92v8upbCvChm6d5wQAAAAG9qjszAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/e5a809fe337adff6f4d4a.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/0160271dbe745b3b02366.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
STATS_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
STREAM_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0160271dbe745b3b02366.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
