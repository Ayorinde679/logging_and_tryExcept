 #if you use the basicConfig() function more than once only the first one will be considered 
#and the rest will be ignored, this is called the root logger,
# for instance if i import leesson2.py in lesson3.py the logging configuration in lesson2.py will be ignored
#and the logging configuration in lesson3.py will be considered because it is the first one to be executed
#i.e with the root logger, you can only log your logging into one file
#the following step avoid that
import os
import logging
import lesson2
#setting the level of the login, to avoid the root logger issue

logger = logging.getLogger(__name__ )
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('lesson3.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)     

def namecheck(name):
    if len(name) < 2:
        logging.debug(f'checking for error "{name} ....')
        return "Invalid Name"
    elif name.isspace():
        logging.debug(f'checking for error "{name} ....')
        return "Invalid Name"
    elif name.isalpha():
        logging.debug(f'checking for error "{name} ....')
        return "Name is Invalid"
    elif name.replace(' ','').isalpha():
        logging.debug(f'checking for error "{name} ....')
        return "Name is Invalid"
    else:
        logging.debug(f'checking for error "{name} ....')
        return "Invalid Name"


print(namecheck("Alexander"))
