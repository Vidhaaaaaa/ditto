from ocr import get_ocr_log
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

COHERE_KEY = os.getenv("COHERE_TRIAL_KEY")

# initialising the cohere client with api key into "co" object
co = cohere.ClientV2(COHERE_KEY)

 