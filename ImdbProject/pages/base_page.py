from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # finding element
    def find_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # clicking element
    def click_element(self, locator, timeout=20):
        element = self.find_element(locator, timeout)
        element.click()

    # sending keys to the element
    def enter_text(self, locator, text, timeout=20):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # getting current_url
    def get_current_url(self):
        return self.driver.current_url
