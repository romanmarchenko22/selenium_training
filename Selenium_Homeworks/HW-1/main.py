import unittest
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class HomeWork1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://158.101.173.161/admin/")
        self.driver.find_element_by_name("username").send_keys("******")
        self.driver.find_element_by_name("password").send_keys("*******")
        self.driver.find_element_by_name("login").submit()

    def test_main_page(self):
        menu_selector = "//*[@id='box-apps-menu']/li"
        len_of_menu_elements_list = len(self.driver.find_elements_by_xpath(menu_selector))

        for item in range(1, len_of_menu_elements_list + 1):
            try:
                WebDriverWait(self.driver, 5).until(
                    expected_conditions.element_to_be_clickable([By.XPATH, f"//*[@id='box-apps-menu']/li[{item}]"])).click()
            except NoSuchElementException:
                print("The element was not found")

    def tearDown(self):
        self.driver.quit()
