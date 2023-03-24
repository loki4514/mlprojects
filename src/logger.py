import logging
import os
from datetime import datetime

# creating a log file where error ha occured and  many more 
Log_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# strftime : data time object into string

logs_path = os.path.join(os.getcwd(),"logs",Log_FILE)

# crate directory to append the logs
os.makedirs(logs_path,exist_ok=True)

Log_FILE_path = os.path.join(logs_path,Log_FILE)

logging.basicConfig(
    filename=Log_FILE_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

