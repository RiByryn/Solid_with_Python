import logging
from pathlib import Path
import os

try:
    fh = logging.FileHandler('logs/log.log')
except FileNotFoundError:
    print("Creating new log file") 
    os.mkdir("logs")
    with open('logs/log.log', 'w') as f:
        f.write('')
    fh = logging.FileHandler('logs/log.log')

logger = logging.getLogger('my app')
logger.setLevel(logging.DEBUG)


        
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(filename)s | %(funcName)20s() | %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)