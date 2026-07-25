import logging  # module provided by python
import os 

def get_logger():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger(__name__) 
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        file_handler = logging.FileHandler("logs/test.log")
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")


        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


    return logger


# 1. debug 2. info 3. warning 4. error 5. critical