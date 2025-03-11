import logging

# Configure logging
logging.basicConfig(
    filename="debug.log",  # Log file name
    level=logging.DEBUG,  # Set logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log format
    filemode="a",  # Append to the log file (use "w" to overwrite each run)
)

# Create a logger instance for modules to use
logger = logging.getLogger("nyt_auto_subscriber_logger")
