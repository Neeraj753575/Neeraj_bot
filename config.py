import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 21265409
API_HASH = "34c826fd1b989c35e338248d07ad3665"
BOT_TOKEN = "7278624463:AAFh3-7nxD2xw_S9lT9-AD0kwVndc-O-BYQ"
MONGO_DB_URI = "mongodb+srv://DxLEGEND143:DxLEGEND143@dxlegend.oztipqk.mongodb.net/?retryWrites=true&w=majority&appName=DxLEGEND"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))
LOG_GROUP_ID = -1002223899421
OWNER_ID = 6559330178

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Learningbots79/Learning_Bots",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/neeraj663")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/neeraj663")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFEfAEAZVKghTaG8KLieBPSXB3XQ71gcMJ6iE6kPLS60Yh0ZfOygXmfQRS3ZkOBUfzLORIe-djwIg7_Pe5pufL9oMoPSJSvJvnpmQjSl9GHgGwmssnhlaC3pJJwkXacypGiPiW5-344VwKx0vyi0TXYM5sCqTDmlZvBiyxmbxVUDUS4o90mpP84_a3DPwG5aZOIQlqytUool8T6sRbCa1-VFzmShczmhGnHBeNFpPRALasdo-7wOmtDO6lKWYBEsp56l3uJ0G6QFyMOfWJnHZHcLvfFtuUPkd4439hlZ36E4rwCDdo3eZQ8lZIdI4WS9m924RgHBrqPBk8P2_IfadqObSHOxwAAAAGG92-CAA"
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
    "START_IMG_URL", "https://graph.org/file/9d65090417dfa95d504be.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/9d65090417dfa95d504be.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/b126f9d541a2126bfb963.jpg"
STATS_IMG_URL = "https://graph.org/file/b126f9d541a2126bfb963.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/7da75d8b6241bb55b4cdd.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/7da75d8b6241bb55b4cdd.jpg"
STREAM_IMG_URL = "https://graph.org/file/7da75d8b6241bb55b4cdd.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b126f9d541a2126bfb963.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/9d65090417dfa95d504be.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/77463f1fa8aefb3aef14a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/7da75d8b6241bb55b4cdd.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/77463f1fa8aefb3aef14a.jpg"


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
