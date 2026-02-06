"""
Configuration Module for Telegram Moderation Bot

This module loads environment variables and defines bot configuration settings
including API credentials, command cooldown, and permission rights for user moderation.

Environment variables should be set in a .env file:
- API_ID: Your Telegram API ID from my.telegram.org
- API_HASH: Your Telegram API Hash from my.telegram.org
- BOT_TOKEN: Your bot token from @BotFather

Author: Divyansh Shakya
"""

import os
from dotenv import load_dotenv
from telethon.tl.types import ChatBannedRights

# Load environment variables from .env file
load_dotenv()

# Telegram API Configuration
# Get these from https://my.telegram.org/apps
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')  # Get from @BotFather

# Bot Settings
COMMAND_COOLDOWN = 2  # Seconds between commands per user (prevents spam)
LOG_FILE = 'bot.log'  # File where bot logs are stored
SESSION_NAME = 'bot_session'  # Telethon session file name

# Rights configurations for moderation actions
# MUTE: User cannot send messages but can view
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

# BAN: User cannot view or send messages
BAN_RIGHTS = ChatBannedRights(until_date=None, view_messages=True, send_messages=True)

# UNBAN: Removes all restrictions
UNBAN_RIGHTS = ChatBannedRights(until_date=None)
