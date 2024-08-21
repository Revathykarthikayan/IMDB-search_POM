import pytest
from selenium import webdriver


# marked fixture
@pytest.fixture(scope="class")
def setup(request):
    # initialising driver
    driver = webdriver.Chrome()
    driver.get("https://www.imdb.com/search/name/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
