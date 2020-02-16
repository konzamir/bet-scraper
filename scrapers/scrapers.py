from scrapers import settings
from scrapers.utils import BaseScraper


class BookmakerScraper(BaseScraper):

    def auth(self):
        self.webdriver.get(settings.BOOKMAKER_AUTH)

        self.set_field_data_by_xpath(
            '//form[contains(@id, "Form2")]//input[contains(@name, "account")]',
            settings.BOOKMAKER_EMAIL,
        )

        self.set_field_data_by_xpath(
            '//form[contains(@id, "Form2")]//input[contains(@name, "password")]',
            settings.BOOKMAKER_PASSWORD,
        )

        self.click_by_xpath(
            '//form[contains(@id, "Form2")]//input[contains(@type, "submit")]',
        )

    def _open_history_tab(self):
        self.click_by_xpath(
            '//i[contains(@class, "fa-history")]',
        )

    def scrape(self) -> list:
        self.auth()
        self._open_history_tab()
        return []
