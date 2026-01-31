import asyncio
from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from commands import register_handlers
from utils import logger

async def main():
    """Initialize and run the bot"""
    try:
        # Initialize client
        client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
        
        # Register all command handlers
        await register_handlers(client)
        
        # Start bot
        await client.start(bot_token=BOT_TOKEN)
        
        print("✅ Bot started successfully!")
        print("💡 Use /status in your group to check bot permissions")
        
        await client.run_until_disconnected()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        logger.error(f"Bot error: {e}")

if __name__ == '__main__':
    asyncio.run(main())
