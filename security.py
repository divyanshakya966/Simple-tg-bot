"""
Security Module for Telegram Moderation Bot

This module provides security functions for the bot including:
- Rate limiting to prevent command spam
- Admin permission checks
- User role verification (admin, creator)
- Bot permission validation

All moderation commands use these functions to ensure secure operation.

Author: Divyansh Shakya
"""

import time
from collections import defaultdict
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
from utils import logger
from config import COMMAND_COOLDOWN

# Rate limiting storage: tracks last command time for each user
user_last_command = defaultdict(float)

def check_rate_limit(user_id):
    """
    Check if user is sending commands too fast.
    
    Prevents command spam by enforcing a cooldown period between commands.
    Each user can only execute one command every COMMAND_COOLDOWN seconds.
    
    Args:
        user_id (int): Telegram user ID
        
    Returns:
        bool: True if user can execute command, False if still in cooldown
    """
    current_time = time.time()
    last_command_time = user_last_command[user_id]
    
    # Check if enough time has passed since last command
    if current_time - last_command_time < COMMAND_COOLDOWN:
        return False
    
    # Update last command time for this user
    user_last_command[user_id] = current_time
    return True

async def check_user_is_admin(client, event):
    """
    Check if the command sender is a group administrator.
    
    This function verifies that the user who sent a command has
    admin or creator privileges in the group.
    
    Args:
        client: Telethon client instance
        event: Message event containing sender and chat information
        
    Returns:
        bool: True if sender is admin or creator, False otherwise
    """
    try:
        sender_id = event.sender_id
        participant = await client(GetParticipantRequest(
            channel=event.chat_id,
            participant=sender_id
        ))
        
        # Check if user is admin or creator
        if isinstance(participant.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)):
            return True
        return False
    except Exception as e:
        logger.error(f"Error checking sender admin status: {e}")
        return False

async def check_user_is_creator(client, chat_id, user_id):
    """
    Check if a user is the group creator.
    
    Group creators have special protection and cannot be moderated
    by the bot, regardless of admin permissions.
    
    Args:
        client: Telethon client instance
        chat_id (int): Chat/group ID
        user_id (int): User ID to check
        
    Returns:
        bool: True if user is the group creator, False otherwise
    """
    try:
        participant = await client(GetParticipantRequest(
            channel=chat_id,
            participant=user_id
        ))
        return isinstance(participant.participant, ChannelParticipantCreator)
    except Exception as e:
        logger.error(f"Error checking creator status: {e}")
        return False

async def check_bot_admin_status(client, chat_id):
    """
    Check if the bot has administrator privileges in a group.
    
    The bot needs admin status to perform moderation actions like
    banning, muting, or kicking users.
    
    Args:
        client: Telethon client instance
        chat_id (int): Chat/group ID
        
    Returns:
        bool: True if bot is admin or creator, False otherwise
    """
    try:
        me = await client.get_me()
        participant = await client(GetParticipantRequest(
            channel=chat_id,
            participant=me.id
        ))
        
        # Check if bot has admin or creator status
        if isinstance(participant.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)):
            return True
        return False
    except Exception as e:
        logger.error(f"Error checking bot admin status: {e}")
        return False

async def check_user_admin_status(client, chat_id, user_id):
    """
    Check if a specific user is a group administrator.
    
    Used to prevent admins from being moderated by other admins.
    Admins and creators are protected from moderation actions.
    
    Args:
        client: Telethon client instance
        chat_id (int): Chat/group ID
        user_id (int): User ID to check
        
    Returns:
        bool: True if user is admin or creator, False otherwise
    """
    try:
        participant = await client(GetParticipantRequest(
            channel=chat_id,
            participant=user_id
        ))
        
        # Check if user is admin or creator
        if isinstance(participant.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)):
            return True
        return False
    except Exception as e:
        logger.error(f"Error checking user admin status: {e}")
        return False
