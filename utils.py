import logging
import time
import sys
from collections import defaultdict

# Setup logging with proper encoding for Windows
def setup_logging():
    # Create formatter without emojis for log files
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # Create formatter for console (handle encoding)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # File handler
    file_handler = logging.FileHandler('bot.log', encoding='utf-8')
    file_handler.setFormatter(file_formatter)
    
    # Console handler with proper encoding
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_formatter)
    
    # Configure root logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logging()

# Moderation logging
moderation_log = []

def log_moderation_action(admin_id, admin_name, action, target_id, target_name, chat_id, success=True):
    """Log all moderation actions for audit trail"""
    log_entry = {
        'timestamp': time.time(),
        'admin_id': admin_id,
        'admin_name': admin_name,
        'action': action,
        'target_id': target_id,
        'target_name': target_name,
        'chat_id': chat_id,
        'success': success
    }
    moderation_log.append(log_entry)
    status = 'SUCCESS' if success else 'FAILED'
    logger.info(f"MODERATION: {admin_name} ({admin_id}) {action} {target_name} ({target_id}) in {chat_id} - {status}")

def get_recent_logs(count=5):
    """Get recent moderation logs"""
    return moderation_log[-count:] if moderation_log else []

def format_log_text(logs):
    """Format logs for display"""
    if not logs:
        return "📋 No moderation actions logged yet."
    
    log_text = "📋 **Recent Moderation Actions:**\n\n"
    for log in logs:
        timestamp = time.strftime('%H:%M:%S', time.localtime(log['timestamp']))
        status = "✅" if log['success'] else "❌"
        log_text += f"{status} `{timestamp}` - {log['admin_name']} {log['action']} {log['target_name']}\n"
    
    return log_text
