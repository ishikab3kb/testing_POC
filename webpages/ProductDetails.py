from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import re


class ProductDetails:
    discount_section = (By.XPATH, "//span[@class='pdp-discount']")
    mrp = (By.XPATH, "//span[@class='pdp-mrp']")
    wishlist_xpath = (By.XPATH, "//span[text()='WISHLIST']")
    signin_xpath = (By.XPATH, "//div[@class='signInContainer']")

    def __init__(self, driver):
        self.driver = driver

    def get_discount_percentage(self):
        windows = self.driver.window_handles
        parent_window = windows[0]
        child_window = windows[1]
        self.driver.switch_to.window(child_window)
        print(self.driver.title)
        time.sleep(10)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span["
                                                                                          "@class='pdp-discount']")))
        mrp_element = self.driver.find_element(*ProductDetails.mrp)
        discount_text = element.get_attribute("textContent")
        discount_value = int(re.findall(r'\d+', discount_text)[0])
        mrp_text = mrp_element.get_attribute("textContent")
        mrp_value = int(re.findall(r'\d+', mrp_text)[0])

        print("MRP is ", mrp_value)
        # print("Discount Price is ", discount_value)

        if "%" in discount_text:
            print("Discount on the selected product is: ", discount_value, "%")
        elif "Rs." in discount_text:
            discount_percent = int(discount_value * 100 / mrp_value)
            print("Discount Percentage for this product is: ", discount_percent, "%")
        time.sleep(10)

    def click_wishlist(self):

        wishlist_ele = self.driver.find_element(*ProductDetails.wishlist_xpath)
        wishlist_ele.click()
        time.sleep(10)


