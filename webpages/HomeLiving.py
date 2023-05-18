from selenium.webdriver.common.by import By


class HomeLiving:
    floor_and_lamps_link = (
        By.XPATH, "//a[contains(@class, 'navi-link') and contains(@class, 'navi-underline') and text("
                  ") = 'Floor Lamps']")

    def __init__(self, driver):
        self.driver = driver

    def click_floor_and_lamps(self):
        self.driver.find_element(*HomeLiving.floor_and_lamps_link).click()

