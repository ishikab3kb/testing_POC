import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    men_section = (By.XPATH, "//a[@data-group='men']")
    women_section = (By.XPATH, "//a[@data-group='women'] ")
    kids_section = (By.XPATH, "//a[@data-group='kids']")
    home_and_living_section = (By.XPATH, "//a[@data-group='home-&-living']")
    # home_and_living_section = (By.XPATH, "//div[@class='desktop-shopLinks']/a[text()='Home & Living']")
    beauty_section = (By.XPATH, "//a[@data-group='beauty']")
    studio_section = (By.XPATH, "//a[@data-group='studio']")
    search_box = (By.XPATH, "//input[@class='desktop-searchBar']")
    wishlist = (By.XPATH, "//a[@class='desktop-wishlist']")
    cart = (By.XPATH, "//a[@class='desktop-cart']")
    online_shopping_links_list = (By.XPATH, "//a[contains(text(),'ONLINE SHOPPING')]//parent::p/following-sibling::a")
    online_shopping_link_before = (By.XPATH, '//*[@id="mountRoot"]/div/main/div/div[18]/div/div/div/div/div['
                                                   '5]/div/div/div/div/div/a')
    home_and_living_link = None

    signin_xpath = (By.XPATH, "//div[@class='welcome-header']")

    def __init__(self, driver):
        self.driver = driver

    def get_section_list(self):
        print("Got all the sections.")
        ele_list = self.driver.find_elements(*HomePage.online_shopping_links_list)
        desired_list = []
        self.home_and_living_link = ele_list[3]
        for i in range(7):
            desired_list.append(ele_list[i].get_attribute('textContent'))
        print(desired_list)

    def click_home_and_living(self):
        # action = ActionChains(self.driver)
        # action.scroll_by_amount(0, 800).perform()
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        online_shop_link_before = self.driver.find_element(*HomePage.online_shopping_link_before)
        self.driver.execute_script("arguments[0].scrollIntoView();", online_shop_link_before)
        time.sleep(7)
        self.home_and_living_link.click()
