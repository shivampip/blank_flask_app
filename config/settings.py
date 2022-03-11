import os 
from dotenv import load_dotenv
from utils import log 


load_dotenv()

KEY= os.environ["KEY"]

KEY2= "KEY__2"



log.info("Running {} server".format(os.environ["FLASK_ENV"]))