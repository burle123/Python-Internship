import logging

logging.basicConfig(filename = 'Logging/practice_2.log', level = logging.DEBUG, filemode= 'w', format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a debug message')