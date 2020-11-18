__Author__ = 'Nikunj'

import logging
import sys
import traceback
from logging.handlers import RotatingFileHandler

log_level = 'INFO'
log_format = '%(asctime)s| %(levelname)s: %(message)s'


def log_initializer():
    root_logger = logging.getLogger()

    file_handler = logging.handlers.RotatingFileHandler(filename='logs/flask.log',
                                                        maxBytes=50 * 1000 * 1000,
                                                        backupCount=20)
    file_handler.setFormatter(logging.Formatter(log_format))
    file_handler.setLevel(log_level)
    root_logger.addHandler(file_handler)

    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    stdout_handler.setFormatter(logging.Formatter(log_format))
    stdout_handler.setLevel(log_level)
    root_logger.addHandler(stdout_handler)
