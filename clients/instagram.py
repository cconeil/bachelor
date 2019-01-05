from selenium import webdriver
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_PATH = os.path.join(PROJECT_ROOT, "chromedriver")

class Instagram:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)

    def get_followers(self, username):
        self.browser.get("https://instagram.com/" + username)
        elements = self.browser.find_elements_by_partial_link_text('followers')
        if len(elements) != 1:
            return None

        spans = elements[0].find_elements_by_tag_name('span')
        if len(spans) != 1:
            return None

        return spans[0].get_attribute('title')