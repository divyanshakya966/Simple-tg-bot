# 🤖 Simple Telegram Moderation Bot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Telethon](https://img.shields.io/badge/Telethon-1.36.0-green.svg)](https://docs.telethon.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A powerful, feature-rich Telegram moderation bot built with **Telethon** and designed with a **modular architecture**. This bot provides comprehensive group management capabilities with enhanced security features, automated welcome/goodbye messages, and detailed user information tracking.

---

## ✨ Features

### 🔐 Security & Protection
- **Rate Limiting** - 2-second cooldown between commands to prevent spam
- **Admin-Only Commands** - All moderation actions restricted to group administrators
- **Creator Protection** - Group creator cannot be moderated by anyone
- **Admin Protection** - Admins cannot moderate other admins
- **Bot Self-Protection** - Bot cannot moderate itself
- **Complete Action Logging** - All moderation actions are logged with timestamps and details

### 👥 User Management
- **Ban/Unban** - Permanently ban or unban users from the group
- **Mute/Unmute** - Restrict or restore user messaging permissions
- **Kick** - Temporarily remove users (they can rejoin)
- **User Info** - Detailed user information including status, verification, and premium status
- **Participant Validation** - Ensures users exist in the group before moderation

### 🎉 Welcome & Goodbye System
- **Automatic Welcome Messages** - Greet new members with a fancy formatted message and image
- **Automatic Goodbye Messages** - Bid farewell to leaving members
- **Manual Welcome Command** - Admins can manually welcome users
- **Manual Goodbye Command** - Admins can remove users with a goodbye message
- **Duplicate Prevention** - Prevents sending multiple welcome/goodbye messages
- **Works for Multiple Events** - Handles user joins, adds, leaves, and kicks

### 📊 User Information
- User ID, name, and username
- Phone number (if available)
- Bot/verified/premium status
- Account restrictions and scam flags
- Real-time online status
- Last seen information

### 🏗️ Architecture
- **Modular Design** - Each feature in its own module for easy maintenance
- **Clean Code** - Well-organized, commented, and follows best practices
- **Error Handling** - Comprehensive error handling with user-friendly messages
- **Scalable** - Easily extendable with new features

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.8+** installed on your system
- A **Telegram Bot Token** (get it from [@BotFather](https://t.me/BotFather))
- **Telegram API credentials** (API ID and API Hash)
  - Get them from [my.telegram.org](https://my.telegram.org/apps)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/divyanshakya966/Simple-tg-bot.git
cd Simple-tg-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install telethon==1.36.0 python-dotenv
```

### 3. Configure Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Edit the `.env` file with your credentials:

```env
API_ID='12345678'
API_HASH='your_api_hash_here'
BOT_TOKEN='your_bot_token_here'
```

**How to Get Credentials:**
- **API_ID & API_HASH**: Visit [my.telegram.org](https://my.telegram.org/apps), login with your phone number, and create a new application
- **BOT_TOKEN**: Message [@BotFather](https://t.me/BotFather) on Telegram, create a new bot using `/newbot`, and copy the token

### 4. Add Welcome Image (Optional)

Place your welcome image as `Welc.jpeg` in the root directory. The bot will use this image for welcome messages. If not found, it will send text-only welcomes.

---

## 🎮 Usage

### Starting the Bot

```bash
python bot.py
```

You should see:
```
✅ Bot started successfully!
💡 Use /status in your group to check bot permissions
```

### Adding Bot to Your Group

1. Add the bot to your Telegram group
2. Promote the bot to **administrator** with the following permissions:
   - Delete messages
   - Ban users
   - Invite users (optional, for welcome messages)
   - Pin messages (optional)
3. Test the bot by typing `/status` in the group

---

## 📝 Commands Reference

### 🛡️ Admin-Only Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/ban` | `/ban @username` or reply to message | Ban a user from the group |
| `/unban` | `/unban @username` or reply to message | Unban a previously banned user |
| `/mute` | `/mute @username` or reply to message | Mute a user (restrict messaging) |
| `/unmute` | `/unmute @username` or reply to message | Unmute a user (restore messaging) |
| `/kick` | `/kick @username` or reply to message | Kick a user (they can rejoin) |
| `/welcome` | `/welcome @username` or reply to message | Manually send welcome message |
| `/goodbye` | `/goodbye @username` or reply to message | Remove user and send goodbye |
| `/logs` | `/logs` | View recent moderation actions |

### 👤 Public Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/help` | `/help` | Show all available commands and features |
| `/status` | `/status` | Check bot status and permissions |
| `/uinfo` | `/uinfo @username` or reply to message | Get detailed user information |

### 💡 Usage Examples

```bash
# Ban a user by username
/ban @spammer

# Mute a user by replying to their message
(reply to user's message) /mute

# Get user info
/uinfo @someone

# Manually welcome a new member
/welcome @newuser

# Remove troublesome user with goodbye
/goodbye @troublemaker

# Check recent moderation logs
/logs
```

---

## 📂 Project Structure

```
Simple-tg-bot/
├── bot.py              # Main entry point - initializes and starts the bot
├── commands.py         # Command handlers - registers all bot commands
├── config.py           # Configuration - environment variables and settings
├── security.py         # Security functions - rate limiting, admin checks
├── moderation.py       # Moderation actions - ban, mute, kick logic
├── user_mgmt.py        # User management - user resolution and validation
├── welcome.py          # Welcome/goodbye - welcome and farewell messages
├── userinfo.py         # User info handler - detailed user information
├── utils.py            # Utilities - logging and helper functions
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables
├── .gitignore         # Git ignore file
├── Welc.jpeg          # Welcome image (customizable)
└── README.md          # This file
```

### Module Descriptions

- **`bot.py`** - Initializes the Telethon client, registers handlers, and starts the bot
- **`commands.py`** - Contains all command handlers and event listeners
- **`config.py`** - Loads environment variables and defines bot configuration
- **`security.py`** - Implements rate limiting and permission checks
- **`moderation.py`** - Handles all moderation actions with proper validation
- **`user_mgmt.py`** - Resolves users from commands and validates group membership
- **`welcome.py`** - Manages welcome/goodbye messages and tracking
- **`userinfo.py`** - Provides detailed user information display
- **`utils.py`** - Logging setup and moderation action tracking

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `API_ID` | Telegram API ID from my.telegram.org | `12345678` |
| `API_HASH` | Telegram API Hash from my.telegram.org | `abc123def456...` |
| `BOT_TOKEN` | Bot token from @BotFather | `1234567890:ABC...` |

### Bot Settings (in `config.py`)

```python
COMMAND_COOLDOWN = 2  # seconds between commands per user
LOG_FILE = 'bot.log'  # log file name
SESSION_NAME = 'bot_session'  # Telethon session name
```

---

## 🎨 Customization

### Customize Welcome Message

Edit the welcome message in `welcome.py` (lines 54-80):

```python
greetings = [
    "🌸 A warm welcome to you!",
    "✨ We're glad to have you here!",
    # Add your own greetings here
]
```

### Customize Welcome Image

Replace `Welc.jpeg` with your own image. Supported formats: JPEG, PNG, GIF.

### Customize Rate Limiting

Edit `COMMAND_COOLDOWN` in `config.py`:

```python
COMMAND_COOLDOWN = 2  # Change to your desired cooldown in seconds
```

---

## 🐛 Troubleshooting

### Bot Not Responding
- Ensure the bot is added as an **administrator** in the group
- Check that the bot has necessary permissions (ban users, delete messages)
- Verify your `.env` file has correct credentials
- Check `bot.log` for error messages

### "Bot is not an admin" Error
- The bot needs to be promoted to administrator in the group
- Use `/status` command to check bot's admin status

### Welcome Messages Not Showing
- Ensure `Welc.jpeg` exists in the root directory
- Check file permissions
- The bot will fallback to text-only if image fails

### Rate Limit Errors
- Users can only use commands once every 2 seconds
- This is intentional to prevent spam
- Adjust `COMMAND_COOLDOWN` in `config.py` if needed

---

## 📊 Features in Detail

### Automatic Welcome System
When a user joins or is added to the group:
- Bot sends a beautiful welcome message with image
- Displays user's name, ID, and username
- Includes a random greeting from predefined messages
- Prevents duplicate welcomes with 30-second tracking

### Automatic Goodbye System
When a user leaves or is removed:
- Bot sends a farewell message
- Thanks them for being part of the community
- Prevents duplicate goodbyes with 30-second tracking

### Comprehensive Logging
All moderation actions are logged:
- Timestamp of action
- Admin who performed the action
- Target user details
- Action type (ban, mute, kick, etc.)
- Success/failure status
- Stored in `bot.log` and in-memory for `/logs` command

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Code Style
- Follow PEP 8 guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Divyansh Shakya**
- GitHub: [@divyanshakya966](https://github.com/divyanshakya966)
- Repository: [Simple-tg-bot](https://github.com/divyanshakya966/Simple-tg-bot)

---

## 🙏 Acknowledgments

- [Telethon](https://github.com/LonamiWebs/Telethon) - MTProto API Telegram client library
- [python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management
- Telegram Bot API and community

---

## 📞 Support

If you encounter any issues or have questions:

1. **Check the [Troubleshooting](#-troubleshooting) section**
2. **Open an issue** on [GitHub Issues](https://github.com/divyanshakya966/Simple-tg-bot/issues)
3. **Read the [Telethon Documentation](https://docs.telethon.dev/)**

---

## 🚀 Future Enhancements

Planned features for future releases:

- [ ] Web dashboard for bot management
- [ ] Custom welcome message templates
- [ ] Scheduled messages
- [ ] Advanced anti-spam filters
- [ ] Multi-language support
- [ ] Database integration for persistent storage
- [ ] Analytics and statistics
- [ ] Custom command aliases
- [ ] Automated moderation rules

---

<div align="center">
  <b>⭐ Star this repository if you find it helpful! ⭐</b>
  <br>
  <sub>Made with ❤️ by Divyansh Shakya</sub>
</div>
