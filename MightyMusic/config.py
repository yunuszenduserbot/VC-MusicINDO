import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/22e0ea77281d18134fe5a.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Yunus-ZEND/VC-MusicINDO")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", None)

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
