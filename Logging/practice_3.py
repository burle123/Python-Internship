import logging

logging.basicConfig(filename = 'Logging/practice_3.log', 
                    level = logging.DEBUG, filemode= 'a', 
                    format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt= '%Y-%m-%d %H:%M:%S')

logging.debug('This is a debug message') 
logging.info('This is an info message')
logging.warning('This is a warning message')    
