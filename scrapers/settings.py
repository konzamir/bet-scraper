import os
from os.path import join

from dotenv import load_dotenv


BASE_PATH = os.getcwd()
load_dotenv(dotenv_path=join(BASE_PATH, '.env'))

BOOKMAKER_EMAIL = os.getenv('BOOKMAKER_EMAIL')
BOOKMAKER_PASSWORD = os.getenv('BOOKMAKER_PASSWORD')
