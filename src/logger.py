import logging
import os
from datetime import datetime

# Create logs directory
LOGS_DIR = 'logs'
os.makedirs(LOGS_DIR, exist_ok=True)

# Define log file with a timestamp
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),  # Logs to file
        logging.StreamHandler()         # Logs to console
    ]
)

def get_logger(name):
    """Create and return a logger instance"""
    return logging.getLogger(name)
