from selenium import webdriver

class Instagram:

    def __init__(self):
        self.service = webdriver.chrome.service.Service('./chromedriver')
        options.add_argument('--headless')
        options = options.to_capabilities()
        driver = webdriver.Remote(service.service_url, options)

    def start():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options = options.to_capabilities()
        driver = webdriver.Remote(service.service_url, options)               
