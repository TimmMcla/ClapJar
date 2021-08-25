from selenium import webdriver




def get_browser(browser, location):
    if browser == "chrome":
        return Page(webdriver.Chrome(location))