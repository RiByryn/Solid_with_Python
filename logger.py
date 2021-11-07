import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('my app')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('logs/log.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(filename)s | %(funcName)20s() | %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)