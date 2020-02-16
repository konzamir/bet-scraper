import os
from os.path import join

from dotenv import load_dotenv


BASE_PATH = os.getcwd()
load_dotenv(dotenv_path=join(BASE_PATH, '.env'))

WEBDRIVER_NAME = os.getenv('WEBDRIVER_NAME')
WEBDRIVER_PATH = join(BASE_PATH, 'download', WEBDRIVER_NAME)

BOOKMAKER_EMAIL = os.getenv('BOOKMAKER_EMAIL')
BOOKMAKER_PASSWORD = os.getenv('BOOKMAKER_PASSWORD')
BOOKMAKER_BASE_URL = 'https://www.bookmaker.eu/en/'
BOOKMAKER_AUTH = BOOKMAKER_BASE_URL + 'loginpage'
