from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class InsertPage(BasePage):
    # locators of each element given
    EXPAND_BUTTON = (By.XPATH, '//span[contains(text(),"Expand all")]')
    NAME_TEXT = (By.XPATH, '//input[@placeholder="e.g. Audrey Hepburn"]')
    BIRTHDAY_TEXT = (By.XPATH, '//input[@placeholder="MM-DD"]')
    AWARDS = (By.XPATH, '//span[contains(text(),"Oscar-Winning")]')
    BIOGRAPHY_TILE = (By.XPATH, '//span[contains(text(), "Biography")]')
    BIOGRAPHY = (By.XPATH, '//input[@placeholder="e.g. Arrested"]')
    GENDER = (By.XPATH, '//span[contains(text(),"Male")]')
    CREDITS = (By.XPATH, '//input[@data-testid="autosuggest-input-test-id-filmography"]')
    ADULT_NAMES = (By.XPATH, '//input[@name="Include"]')
    SEARCH_BUTTON = (By.XPATH, '//span[contains(text(),"See results")]')

    def __init__(self, driver):
        # passing driver as parameter to the constructor
        super().__init__(driver)
        # initialising action chains
        self.actions = ActionChains(driver)

    def expand_all(self):
        # Wait for the expand button to be clickable, then click it
        try:
            self.click_element(self.EXPAND_BUTTON)
            self.driver.execute_script("window.scrollBy(0, 1000);")
        except TimeoutException:
            print(f"An error occurred: {TimeoutException}")
        except NoSuchElementException:
            print(f"An error occurred: {NoSuchElementException}")

    def add_name(self, name):
        # Wait for the name text field  to be clickable, then send keys to it
        try:
            self.enter_text(self.NAME_TEXT, name)
            print("Input- Name given")
        except NoSuchElementException:
            print(f"An error occurred: {NoSuchElementException}")

    def add_birthday(self, birthday):
        # Wait for the birthday field to be located, then send keys to it
        try:
            self.enter_text(self.BIRTHDAY_TEXT, birthday)
            print("Input - Birthday given")
        except NoSuchElementException:
            print(f"An error occurred: {NoSuchElementException}")

    def add_award(self):
        # Wait for the awards button to be clickable
        try:
            element = self.find_element(self.AWARDS)
            self.actions.move_to_element(element).click().perform()
            print("Oscar-nominated is selected")
        except NoSuchElementException:
            print(f"An error occurred: {NoSuchElementException}")

    def add_gender(self):
        # Wait for the MALE button to be clickable
        try:
            element = self.find_element(self.GENDER)
            self.actions.move_to_element(element).click().perform()
            print("GENDER is selected")
        except NoSuchElementException:
            print(f"An error occurred: {NoSuchElementException}")

    def add_biography(self, biography):
        # Wait for the  biography to be located, then send keys to it
        try:
            bio_tile_element = self.find_element(self.BIOGRAPHY_TILE)
            self.actions.move_to_element(bio_tile_element).click().perform()
            print("BIOGRAPHY tile is selected")
            self.enter_text(self.BIOGRAPHY, biography)
            print("Input - biography given")
        except NoSuchElementException:
            print(f"An error occurred: {NoSuchElementException}")

    def add_credits(self, credit):
        # Wait for the credits to be located, then send keys to it
        try:
            self.enter_text(self.CREDITS, credit)
            self.actions.send_keys('\t').send_keys('\n').perform()
            print("Credits given")
            self.driver.execute_script("window.scrollBy(0, 3000);")
        except NoSuchElementException:
            print(f"An error occurred: {NoSuchElementException}")

    def search_button(self):
        # Wait for the search button to be clickable
        try:
            self.click_element(self.SEARCH_BUTTON)
            print("See Results button is clicked")


        except NoSuchElementException:
            print(f"An error occurred: {NoSuchElementException}")

    def assert_search_page(self):
        # Check if the specified string is in the current URL
        current_url = self.driver.current_url
        expected_string = "https://www.imdb.com/search/name/?name=A%20R%20R"

        assert expected_string in current_url, f"Expected '{expected_string}'but got {current_url}"
        print("Assertion passed: The search page is loaded correctly in the current URL")
