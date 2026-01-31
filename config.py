import os
from dotenv import load_dotenv
from telethon.tl.types import ChatBannedRights

load_dotenv()

# Telegram API Configuration
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Bot Settings
COMMAND_COOLDOWN = 2  # seconds between commands per user
LOG_FILE = 'bot.log'
SESSION_NAME = 'bot_session'

# Rights configurations
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
BAN_RIGHTS = ChatBannedRights(until_date=None, view_messages=True, send_messages=True)
UNBAN_RIGHTS = ChatBannedRights(until_date=None)
