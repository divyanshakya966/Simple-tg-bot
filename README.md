# Telegram Moderation Bot (Modular Architecture)

A robust, modular Telegram moderation bot with enhanced security features.

## Features
- 🔐 Admin-only moderation commands
- ⏱️ Rate limiting
- 📋 Complete action logging
- 👑 Creator & admin protection
- 🎉 Welcome messages
- 🏗️ Modular architecture

## File Structure
- `bot.py` - Main entry point
- `config.py` - Configuration settings
- `security.py` - Security functions
- `user_management.py` - User resolution
- `moderation.py` - Moderation actions
- `commands.py` - Command handlers
- `utils.py` - Logging utilities

## Setup
1. Copy `.env.example` to `.env` with your credentials
2. `pip install -r requirements.txt`
3. `python bot.py`
4. Add bot to group as admin

## Commands
- `/ban`, `/unban`, `/mute`, `/unmute`, `/kick` (Admin only)
- `/help`, `/status` (Public)
- `/logs` (Admin only)
