from robot.api.deco import keyword

from robot.api import logger
import Browser 
from libraries.LibraryBase import LibraryBase
from libraries.utils import (
    debug,
    run_kw,
    get_variable,
)
import time
import os
import urllib.parse
from resources.locators import JiraLocators
from Browser.utils.data_types import ElementState, SupportedBrowsers
from datetime import timedelta

import os
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

WAIT_TIME = timedelta(minutes=1)

class JiraLibrary(LibraryBase):

    def __init__(self):
        super().__init__()
        self.env = get_variable("${ENV}") 
        self.browser = Browser.Browser()
        self.download_path = get_variable("${download_path}")


    @keyword
    def navigate_to_page(self, domain):
        self.browser.new_browser(browser=SupportedBrowsers.chromium, headless=False, downloadsPath=self.download_path)
        self.browser.new_context(
            acceptDownloads=True,
            viewport={"width": 900, "height": 900},
        )
        url = domain + "/secure/admin/CloudExport.jspa"
        self.browser.new_page(url)
        time.sleep(5)
   

    @keyword
    def insert_username_jira(self, username_jira):
        self.browser.fill_text(JiraLocators.username_selector_jira, username_jira )


    @keyword
    def insert_password_jira(self, password_jira):
        self.browser.fill_text(JiraLocators.password_selector_jira, password_jira)


    @keyword
    def click_sign_in_jira(self):
        self.browser.click(JiraLocators.sign_in_button_jira)


    @keyword
    def get_download_link(self):
        self.browser.wait_for_elements_state(JiraLocators.download_element, ElementState.visible, timeout=WAIT_TIME)
        domain = "https://skaler-sandbox-171.atlassian.net"
        css_selector = "a#download-backup-link-cloud"
        href = self.browser.get_attribute(css_selector, "href")
        download_link = domain+href
        return download_link


    @keyword
    def create_JIRA_download(self):
        self.browser.wait_for_elements_state(JiraLocators.create_backup_button, ElementState.visible, timeout=WAIT_TIME)
        self.browser.click(JiraLocators.create_backup_button) 


    @keyword
    def download_jira(self, download_link):
        promise = self.browser.promise_to_wait_for_download(os.path.join(self.download_path, "backup.zip"))
        self.browser.click(JiraLocators.download_element)
        self.browser.wait_for(promise)


    @keyword
    def send_slack_message(self, domain):
        SLACK_BOT_TOKEN = get_variable("${SLACK_BOT_TOKEN}")
        client = WebClient(token=SLACK_BOT_TOKEN)
        channel_id = "atlassian-products-backup"
        message = f"Atlassian backup is ready for {domain} "
        try:
            response = client.chat_postMessage(
                channel=channel_id,
                text=message
            )
            print(f"Message sent: {response['ts']} -> {message}")
        except SlackApiError as e:
            print(f"Error sending message: {e}")


    @keyword
    def close_jira(self):
        self.browser.close_browser()


    @keyword
    def debug_library(self):
        logger.info(f"{self.__class__}")
        debug()


    @keyword
    def do_something(self):
        run_kw("Log", f"Doing something in {self.env}")
