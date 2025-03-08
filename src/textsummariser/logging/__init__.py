import os
import logging
import sys

# Define log directory and file path
log_dir = "logs"
log_str = "%(asctime)s - %(levelname)s - %(module)s - %(message)s"  
log_filepath = os.path.join(log_dir, "continuos_logs.log")

# Create log directory if not exists
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format=log_str, 
    handlers=[logging.FileHandler(log_filepath), logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("textsummariserlogger")

# Test log message
logger.info("Logging is implemented successfully!")
