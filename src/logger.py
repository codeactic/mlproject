import logging
import os
from datetime import datetime


LOG_FILE=F"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)  #keep on appending the file 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(              #we are overridding the the function for setting our address
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
