import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

EVAL = list(map(int, getenv("EVAL", "6253265083 6253265083").split()))
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","harsh_un")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "KIRA_PROBOT")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "神 𝗞ɪʀᴀ")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "UNB")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002040932096))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 6253265083))
# -----------------------------------------------------------------
# -----------------------------------------------------------------
DEV_ID = int(getenv("DEV_ID", 6253265083))
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/un-bots/cronus",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kira_update")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/unb_support")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQF1d1AAafj0sFjd7ywihWSQPUB5F1lbjZFfeLonQin_E95aJFkZX7xPqtDQGF3dV02Es9kxf5O-vlta9SOyNiLtc60UrpI3n6F12EcqzVgUoOz1r9LmNUaBah641SdQihvq0hM31_nZRfgFOI3YccFZuB_ZyoumWgG2LgBgJ-dhKuF7AJV1Hoo7yE_50srus4SHq-LcqSb0QtelWWJIdRwUS6kEeJmGIp33TZFpJrjAR4v3-6f7NfB5_3sJ-3fPTDj8HoHnw93XnMuJyPLlrQmsrXPqIH1hZFcJ8dQ0RO-suJDeObhBBw0XeY73xO6y8bUD03L6MGduoOJNTyKEuh1iHnTdIAAAAAGYBb4NAA")
STRING2 = getenv("STRING_SESSION2", "BQF64-sAppV4ElYT8r6vodSA4EEGA4119jXaATGHj7zmNIblJivEyJ4uF5yNWjexYbkplKPy0g0ID06a1INOww1Pw_PryyoPftnyoubncEoAvwwwgVNngM8RmkltiwB4QcRWKYKsD6_Q3q39PV1HgfCJFZxJHWjZxY6stQlOP8XzIxQAMxg20Mmu02n8R54Z3PTDNpFCJrCwCnbaSM4u8MRl7CzVz0x2bsWdljMqC7_bvL24054dwVD0x0lqHD-m0lBlcDzsZErW70otu8YeuFr-Ji3QDsobkPZMiaYKjmZrd_9-hHedQ59gAg_E1W0K8XvF4Jqhgo5C0VJ3P5TKUtICmCBQAAAAG0EGmkAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/0fb5799f17005b83a8d14.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/0fb5799f17005b83a8d14.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/0fb5799f17005b83a8d14.jpg"
STATS_IMG_URL = "https://telegra.ph/file/0fb5799f17005b83a8d14.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/0fb5799f17005b83a8d14.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/0fb5799f17005b83a8d14.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/0fb5799f17005b83a8d14.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
