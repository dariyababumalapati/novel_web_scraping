import logging
import os
from datetime import datetime

def setup_logging():
    # Create log directory if it doesn't exist
    log_dir = 'log'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    current_run_log_file = os.path.join(log_dir, 'current.log')

    # Delete the current log file if it exists
    if os.path.exists(current_run_log_file):
        os.remove(current_run_log_file)

    # # Create file handler for current run
    # current_run_log_file = os.path.join(log_dir, f'scrapy_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    # current_run_file_handler = logging.FileHandler(current_run_log_file)
    # current_run_file_handler.setLevel(logging.DEBUG)
    # current_run_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # Create file handler for continuous logs
    continuous_log_file = os.path.join(log_dir, 'continuous_scrapy_log.log')
    continuous_file_handler = logging.FileHandler(continuous_log_file)
    continuous_file_handler.setLevel(logging.DEBUG)
    continuous_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    continuous_log_file = os.path.join(log_dir, 'current.log')
    continuous_file_handler = logging.FileHandler(continuous_log_file)
    continuous_file_handler.setLevel(logging.DEBUG)
    continuous_file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # Create stream handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # Get root logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Add handlers to the logger
    # logger.addHandler(current_run_file_handler)
    logger.addHandler(continuous_file_handler)
    logger.addHandler(console_handler)

    logging.info("Logging setup complete. Log files are located in the 'log' directory.")

if __name__ == '__main__':
    setup_logging()
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")