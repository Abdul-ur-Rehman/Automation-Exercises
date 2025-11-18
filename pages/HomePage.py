from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        self.home_verification_test_loc = (By.XPATH,"//h1[contains(.,'Auto')]")
        self.login_button_loc = (By.LINK_TEXT,"Signup / Login")
        self.logged_in_user_loc = (By.XPATH, "//ul//a[starts-with(.,' Logged')]")




    def homePage_verification(self):
        verification_text = self.driver.find_element(*self.home_verification_test_loc).text
        print(verification_text)
        return verification_text

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()
        login_Page = LoginPage(self.driver)
        return login_Page

    def logged_in_user(self):

        account_logged = self.driver.find_element(*self.logged_in_user_loc).text
        print(account_logged)
        return account_logged
