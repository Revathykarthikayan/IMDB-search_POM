import pytest
from pages.insert_page import InsertPage


# calling every method of insert page
@pytest.mark.usefixtures("setup")
class TestInsertPage:
    def test_insert_page(self):
        insert_page = InsertPage(self.driver)

        insert_page.expand_all()
        insert_page.add_name("A R Rahman")
        insert_page.add_birthday("06-01-1967")
        insert_page.add_biography("Notes of a Dream")
        insert_page.add_gender()
        insert_page.add_credits("Slumdog Millionaire")
        insert_page.add_award()
        insert_page.search_button()
        insert_page.assert_search_page()
