from telethon import events
from security import check_rate_limit, check_user_is_admin, check_bot_admin_status
from user_mgmt import get_user_from_event
from moderation import moderate_user
from utils import get_recent_logs, format_log_text, logger
from config import BAN_RIGHTS, MUTE_RIGHTS, UNBAN_RIGHTS
from welcome import register_welcome_handler, send_fancy_welcome
from userinfo import register_userinfo_handler

async def register_handlers(client):
    """Register all command handlers"""
    
    # CLEANED Welcome handler - no unnecessary logs
    @client.on(events.ChatAction)
    async def handle_welcome(event):
        try:
            # Process both user_joined and user_added events
            if not (event.user_joined or event.user_added):
                return
            
            new_user = None
            
            # Get the action from the event
            if hasattr(event, 'action_message') and event.action_message:
                action_msg = event.action_message
                
                # Case 1: User joined by themselves
                if event.user_joined and hasattr(action_msg, 'from_id'):
                    try:
                        new_user = await client.get_entity(action_msg.from_id)
                    except Exception:
                        pass  # Silent fail, no logging
                
                # Case 2: User was added by someone else
                elif event.user_added and hasattr(action_msg, 'action') and hasattr(action_msg.action, 'users'):
                    try:
                        # Get the first user from the action (newly added)
                        new_user_id = action_msg.action.users[0]
                        new_user = await client.get_entity(new_user_id)
                    except Exception:
                        pass  # Silent fail, no logging
            
            # If we found a new user, welcome them instantly
            if new_user:
                try:
                    chat = await event.get_chat()
                    await send_fancy_welcome(client, chat, new_user)
                    logger.info(f"Welcomed: {new_user.first_name} ({new_user.id})")
                except Exception as e:
                    logger.error(f"Error sending welcome: {e}")
            
            # No logging if user not found - this eliminates spam
                        
        except Exception as e:
            logger.error(f"Welcome handler error: {e}")

    # All moderation commands remain exactly the same...
    @client.on(events.NewMessage(pattern=r'^/ban'))
    async def ban_cmd(event):
        if not check_rate_limit(event.sender_id):
            await event.reply("⏱️ Please wait before using another command.")
            return
        
        if not await check_user_is_admin(client, event):
            await event.reply("❌ Only admins can use this command.")
            return
        
        user = await get_user_from_event(client, event)
        if user:
            await moderate_user(client, event, user, "banned", BAN_RIGHTS)

    @client.on(events.NewMessage(pattern=r'^/unban'))
    async def unban_cmd(event):
        if not check_rate_limit(event.sender_id):
            await event.reply("⏱️ Please wait before using another command.")
            return
        
        if not await check_user_is_admin(client, event):
            await event.reply("❌ Only admins can use this command.")
            return
        
        user = await get_user_from_event(client, event)
        if user:
            await moderate_user(client, event, user, "unbanned", UNBAN_RIGHTS)

    @client.on(events.NewMessage(pattern=r'^/mute'))
    async def mute_cmd(event):
        if not check_rate_limit(event.sender_id):
            await event.reply("⏱️ Please wait before using another command.")
            return
        
        if not await check_user_is_admin(client, event):
            await event.reply("❌ Only admins can use this command.")
            return
        
        user = await get_user_from_event(client, event)
        if user:
            await moderate_user(client, event, user, "muted", MUTE_RIGHTS)

    @client.on(events.NewMessage(pattern=r'^/unmute'))
    async def unmute_cmd(event):
        if not check_rate_limit(event.sender_id):
            await event.reply("⏱️ Please wait before using another command.")
            return
        
        if not await check_user_is_admin(client, event):
            await event.replies("❌ Only admins can use this command.")
            return
        
        user = await get_user_from_event(client, event)
        if user:
            await moderate_user(client, event, user, "unmuted", UNBAN_RIGHTS)

    @client.on(events.NewMessage(pattern=r'^/kick'))
    async def kick_cmd(event):
        if not check_rate_limit(event.sender_id):
            await event.reply("⏱️ Please wait before using another command.")
            return
        
        if not await check_user_is_admin(client, event):
            await event.reply("❌ Only admins can use this command.")
            return
        
        user = await get_user_from_event(client, event)
        if user:
            await moderate_user(client, event, user, "kick", None)

    # Public commands
    @client.on(events.NewMessage(pattern=r'^/help'))
    async def help_cmd(event):
        help_text = """
    🤖 **Moderation Bot Commands:**
    
    
**Admin Only Commands:**
• `/ban` - Ban user (reply or @username)
• `/unban` - Unban user  
• `/mute` - Mute user (reply or @username)
• `/unmute` - Unmute user
• `/kick` - Kick user (reply or @username)
• `/welcome` - Send custom welcome (reply or @username)
• `/goodbye` - Remove user & send goodbye (reply or @username)


**Public Commands:**
• `/help` - Show this help
• `/status` - Check bot status  
• `/uinfo` - Get user info (reply or @username)


**Usage Examples:**
• `/ban @username`
• `/mute` (reply to message)
• `/kick @spammer`
• `/uinfo @someone`
• `/welcome @newuser`
• `/goodbye @troublemaker`


**Features:**
• ✅ Auto-welcome messages (join & add)
• ✅ Auto-goodbye messages (leave & remove)
• ✅ Admin-only moderation commands  
• ✅ Human-readable user status display
• ✅ Rate limiting (2sec cooldown)
• ✅ Creator protection
• ✅ Admin protection
• ✅ Duplicate message prevention
• ✅ Complete action logging


**Welcome/Goodbye System:**
• 🌸 Fancy welcome with image & user info
• 👋 Personalized goodbye messages
• 🔄 Works for joins, adds, leaves, kicks
• 🛡️ Duplicate prevention system
    """
        await event.reply(help_text)

    @client.on(events.NewMessage(pattern=r'^/status'))
    async def status_cmd(event):
        try:
            me = await client.get_me()
            is_admin = await check_bot_admin_status(client, event.chat_id)
            user_is_admin = await check_user_is_admin(client, event)
            
            status_text = f"""
🤖 **Bot Status:**
• Bot ID: `{me.id}`
• Username: @{me.username}
• Bot Admin Status: {'✅ Yes' if is_admin else '❌ No'}
• Your Admin Status: {'✅ Yes' if user_is_admin else '❌ No'}
• Chat ID: `{event.chat_id}`
• Rate Limiting: ✅ Active
• Action Logging: ✅ Active
• Clean Welcome: ✅ Active

{('⚠️ **Bot needs admin privileges!**' if not is_admin else '✅ **Bot ready to moderate!**')}
            """
            await event.reply(status_text)
        except Exception as e:
            await event.reply(f"Status check failed: {e}")

    @client.on(events.NewMessage(pattern=r'^/logs'))
    async def logs_cmd(event):
        if not await check_user_is_admin(client, event):
            await event.reply("❌ Only admins can view logs.")
            return
        
        logs = get_recent_logs()
        log_text = format_log_text(logs)
        await event.reply(log_text)

    # Register new handlers
    await register_welcome_handler(client)
    await register_userinfo_handler(client)
