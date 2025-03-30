import logging
import os
from logging.handlers import TimedRotatingFileHandler

import utils.config as config


def setup_logger():
    """
    Configure the global logger.
    """
    # Create a log directory
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup format
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    formatter = logging.Formatter(log_format)

    # Daily backup
    log_file = os.path.join(log_dir, "app.log")
    file_handler = TimedRotatingFileHandler(
        log_file, when="midnight", interval=1, backupCount=7
    )
    file_handler.setFormatter(formatter)
    file_handler.suffix = "%Y-%m-%d"

    # Console Processor
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Initialize logging
    logger = logging.getLogger()
    logger.setLevel(config.LOGGING_LEVEL)

    # Add logging handler
    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)

    # custom logging level for specific module
    # module_logger = logging.getLogger("SetupWindow")
    # module_logger.setLevel(config.SETUP_MODULE_LOGGING_LEVEL)

    return logger
