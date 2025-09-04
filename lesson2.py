#using the loging function instead of print
import logging 
#setting the level of the login
logging.basicConfig(filename="demo.log",level=logging.DEBUG, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
#Note:filemode='w' is used to overwrite the log file each time the code is run
#NOTE: the default level of logging is warning
#to disable logging messages
#logging.disable()
""" in the logging module there are different levels of logging and they are in this 
heirarchy order:
1. debug: detailed information, typically of interest only when diagnosing problems, 
it is the lowest level
2. info: confirmation that things are working as expected
3. warning: an indication that something unexpected happened, or indicative of some 
problem in the near future
4. error: due to a more serious problem, the software has not been able to perform 
some function
5. critical: a serious error, indicating that the program itself may be unable to 
continue running"""


def namecheck(name):
    if len(name) < 2:
        logging.debug("checking for debugging....")
        return "Invalid Name"
    elif name.isspace():
        logging.debug("checking if name is a space..")
        return "Invalid Name"
    elif name.isalpha():
        logging.debug("checking if name is an alphabet.")
        return "Name is Invalid"
    elif name.replace(' ','').isalpha():
        logging.debug("checking for full name.")
        return "Name is Invalid"
    else:
        logging.debug("failed all check...")
        return "Invalid Name"


print(namecheck("Alexander"))