import logging

logging.basicConfig(
    filename='multilogger_msg.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

lg1=logging.getLogger("module1")
lg2=logging.getLogger("module2")

lg1.debug("logging msg from module 1")
lg2.debug("logging msg from module 2")
