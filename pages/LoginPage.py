from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.login_page_verfication_loc = (By.XPATH, "//h2[text()='New User Signup!']")
        self.login_name_loc = (By.NAME, "name")
        self.login_email_loc = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signup_button_loc = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def login_page_verification(self):
        return self.driver.find_element(*self.login_page_verfication_loc).text

    def account_signup(self, name, email):
        self.driver.find_element(*self.login_name_loc).send_keys(name)
        self.driver.find_element(*self.login_email_loc).send_keys(email)
        self.driver.find_element(*self.signup_button_loc).click()
        accountPage = AccountPage(self.driver)
        return accountPage




