import abc

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from scrapers import settings


class SeleniumMixin:
    webdriver = None
    wait_timeout = 20
    sleep_input_time = 5

    def setup_webdriver(self):
        print('Connecting webdriver...')
        options = webdriver.ChromeOptions()

        self.webdriver = webdriver.Chrome(
            executable_path=settings.WEBDRIVER_PATH,
            chrome_options=options
        )

    def close_webdriver(self):
        print('Closing webdriver...')
        self.webdriver.close()

    def get_element_by_id(self, id_data: str, timeout=None, *args, **kwargs):
        try:
            timeout = timeout or self.wait_timeout
            return WebDriverWait(self.webdriver, timeout).until(
                EC.element_to_be_clickable((By.ID, id_data))
            )

        except TimeoutException:
            print(f'Could not load id {id_data}!')
            return None

    def get_element_by_xpath(self, xpath_data: str, timeout=None, *args, **kwargs):
        try:
            timeout = timeout or self.wait_timeout
            return WebDriverWait(self.webdriver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath_data))
            )
        except TimeoutException:
            print(f'Could not load xpath {xpath_data} field!')
            return None

    def set_field_data_by_id(self, field_id: str, data: str, *args, **kwargs):
        field = self.get_element_by_id(field_id, *args, **kwargs)
        if field:
            self.webdriver.implicitly_wait(self.sleep_input_time)
            field.send_keys(data)

    def set_field_data_by_xpath(self, field_xpath: str, data: str, *args, **kwargs):
        field = self.get_element_by_xpath(field_xpath, *args, **kwargs)
        if field:
            self.webdriver.implicitly_wait(self.sleep_input_time)
            field.send_keys(data)

    def click_by_xpath(self, field_xpath: str, *args, **kwargs):
        button = self.get_element_by_xpath(
            field_xpath, *args, **kwargs
        )
        if button:
            button.click()


class BaseScraper(abc.ABC, SeleniumMixin):

    def __init__(self):
        self.setup_webdriver()

    @abc.abstractmethod
    def auth(self):
        pass

    @abc.abstractmethod
    def scrape(self) -> list:
        pass
