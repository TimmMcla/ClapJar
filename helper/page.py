from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains as AC
from selenium.webdriver.common.keys import Keys


class Page(object):
    __TIMEOUT = 10

    def __init__(self, driver):
        self.driver_wait = WebDriverWait(driver, Page.__TIMEOUT)
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)
    
    def send_keys(self, string):
        self.driver.send_keys(string)

    def send_keys(self, keys):
        self.driver.send_keys(keys)