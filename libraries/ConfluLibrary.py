from robot.api.deco import keyword

from robot.api import logger
import Browser 
from libraries.LibraryBase import LibraryBase
from libraries.utils import (
    debug,
    run_kw,
    get_variable,
)
from Browser.utils.data_types import SupportedBrowsers
import time

from resources.locators import JiraLocators

class ExcelLibrary(LibraryBase):


    def __init__(self):
        super().__init__()
        self.env = get_variable("${ENV}")
        self.browser = Browser.Browser()

    @keyword
    def navigate_pages(self, urls):
        self.browser.new_browser(browser=SupportedBrowsers.chromium, headless=False)
        self.browser.new_context(
            acceptDownloads=True,
            viewport={"width": 900, "height": 900},
        )
        self.browser.new_page(urls[0])
        time.sleep(5)
   
    @keyword
    def insert_username_conflu(self, username_conflu):
        self.browser.fill_text(JiraLocators.username_selector_conflu, username_conflu )

    @keyword
    def insert_password_conflu(self, password_conflu):
        self.browser.fill_text(JiraLocators.password_selector_conflu, password_conflu)

    @keyword
    def click_sign_in_conflu(self):
        self.browser.click(JiraLocators.JiraLocators_button_conflu)

    @keyword
    def debug_library(self):
        logger.info(f"{self.__class__}")
        debug()

    @keyword
    def do_something(self):
        run_kw("Log", f"Doing something in {self.env}")
