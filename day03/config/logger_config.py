# configure log format
import logging
"""
set up a logger for healthcare application, which will log messages to a file named 'healthcare.log' with a log level of DEBUG. The logger will be named 'healthcare_logger'. If the logger already has handlers, it will return the existing logger instead of creating a new one.
"""

def setup_logger():
    """Create a logger for the healthcare application."""

    logger = logging.getLogger('healthcare_logger')
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        return logger

    file_handler = logging.FileHandler('healthcare.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.propagate = False
    return logger

   