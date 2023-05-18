import pytest
import time

from webpages.HomePage import HomePage
from webpages.HomeLiving import HomeLiving
from webpages.FloorLamp import FloorLamp
from webpages.ProductDetails import ProductDetails


@pytest.mark.usefixtures("setup")
class TestSample:
    def test_check_browser_functionality(self):
        home_page = HomePage(self.driver)
        time.sleep(5)
        home_page.get_section_list()
        print("Successfully ran the first test case")
        home_page.click_home_and_living()
        home_living = HomeLiving(self.driver)
        # time.sleep(5)
        home_living.click_floor_and_lamps()
        floor_lamps = FloorLamp(self.driver)
        # time.sleep(5)
        parent_window = self.driver.title
        floor_lamps.select_and_click_product()

        product_page = ProductDetails(self.driver)
        time.sleep(5)

        product_page.get_discount_percentage()
        new_window = self.driver.title

        if parent_window != new_window:
            print("Product was opened in new window.")
        else:
            print("Testcase failed")

        product_page.click_wishlist()

        current_url = self.driver.current_url
        if "login" in current_url:
            print("Login prompt opened successfully")
        else:
            print("Prompt opening failed.")

        # signin_ele = self.driver.find_element(*HomePage.signin_xpath)
        # print(signin_ele.get_attribute("textContent"))
