from logger import logging
def add(a,b):
    logging.debug("this is add operation function")
    return a+b

logging.debug("addition function is called")
add(10,20)