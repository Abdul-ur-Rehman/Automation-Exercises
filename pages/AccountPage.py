from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AccountPage:

    def __init__(self,driver):
        self.driver = driver

        self.accountPage_verification_text_loc = (By.XPATH,"//h2[starts-with(.,'Enter')]")
        self.gender_loc = (By.CSS_SELECTOR, "input[id='id_gender1']")
        self.password_loc = (By.XPATH,"//input[@data-qa='password']")
        self.days_loc = (By.ID, "days")
        self.months_loc = (By.ID, "months")
        self.years_loc = (By.ID, "years")
        self.newsletter_loc = (By.NAME, "newsletter")
        self.optin_loc = (By.NAME, "optin")
        self.firstname_loc = (By.ID, "first_name")
        self.lastname_loc = (By.ID, "last_name")
        self.company_loc = (By.ID, "company")
        self.address_loc = (By.ID, "address1")
        self.country_loc = (By.ID, "country")
        self.state_loc = (By.ID, "state")
        self.city_loc = (By.ID, "city")
        self.zipcode_loc = (By.ID, "zipcode")
        self.mobile_number_loc = (By.ID, "mobile_number")
        self.create_account_button_loc = (By.XPATH, "//button[@data-qa='create-account']")
        self.continue_button_loc = (By.XPATH, "//a[@data-qa='continue-button']")
        self.delete_account_button_loc = (By.LINK_TEXT, "Delete Account")
        self.delete_account_verification_text_loc = (By.XPATH, "//h2[starts-with(.,'Acc')]")




    def accountPage_verification(self):
        account_info = self.driver.find_element(*self.accountPage_verification_text_loc).text
        print(account_info)
        return account_info

    def account_detials_form_filling(self, password):

        self.driver.find_element(*self.gender_loc).click()
        self.driver.find_element(*self.password_loc).send_keys(password)

        Select(self.driver.find_element(*self.days_loc)).select_by_value("10")
        month_dropdown = self.driver.find_element(*self.months_loc)
        month_obj = Select(month_dropdown)
        month_obj.select_by_value("9")
        Select(self.driver.find_element(*self.years_loc)).select_by_value("1998")

        self.driver.find_element(*self.newsletter_loc).click()
        self.driver.find_element(*self.optin_loc).click()

        self.driver.find_element(*self.firstname_loc).send_keys("Abdur")
        self.driver.find_element(*self.lastname_loc).send_keys("Rehman")
        self.driver.find_element(*self.company_loc).send_keys("AR Ltd")
        self.driver.find_element(*self.address_loc).send_keys("abd123 PO 123")
        Select(self.driver.find_element(*self.country_loc)).select_by_index(1)
        self.driver.find_element(*self.state_loc).send_keys("California")
        self.driver.find_element(*self.city_loc).send_keys("California")
        self.driver.find_element(*self.zipcode_loc).send_keys("CA123")
        self.driver.find_element(*self.mobile_number_loc).send_keys("090078601")

        self.driver.find_element(*self.create_account_button_loc).click()

        account_creation_confirmation = self.driver.find_element(By.XPATH, "//h2[starts-with(.,'Account Created!')]").text
        print(account_creation_confirmation)
        return account_creation_confirmation

    def continue_to_HomePage(self):
        return self.driver.find_element(*self.continue_button_loc).click()

    def delete_account(self):

        self.driver.find_element(*self.delete_account_button_loc).click()
        account_deleted_verification = self.driver.find_element(*self.delete_account_verification_text_loc).text
        print(account_deleted_verification)
        return account_deleted_verification