import time
import random
import pytest
from selenium.webdriver.common.by import By


class FloorLamp:
    search_results = (By.XPATH, "//li[@class='product-base']/child::a")

    def __init__(self, driver):
        self.driver = driver

    def select_and_click_product(self):

        search_results_elements = self.driver.find_elements(*FloorLamp.search_results)
        # print(len(search_results_elements))
        item_no = random.randint(1, len(search_results_elements))
        search_results_elements[item_no].click()
        time.sleep(10)


