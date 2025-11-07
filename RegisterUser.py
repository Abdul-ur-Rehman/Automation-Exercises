import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

email = 'abdulurrehman@abc.com'
name = 'Abdul-ur-Rehman'
password = 'abc123'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver =  webdriver.Chrome(options=options)

driver.get('http://automationexercise.com')

verification_text = driver.find_element(By.XPATH,"//h1[contains(.,'Auto')]").text
print(verification_text)
assert verification_text == 'AutomationExercise'

driver.find_element(By.LINK_TEXT,"Signup / Login").click()
new_user = driver.find_element(By.XPATH,"//h2[text()='New User Signup!']").text

assert new_user == 'New User Signup!'

driver.find_element(By.NAME, "name").send_keys(name)
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)

driver.find_element(By.CSS_SELECTOR,"button[data-qa='signup-button']").click()


account_info = driver.find_element(By.XPATH,"//h2/b[starts-with(.,'Enter')]").text
print(account_info)
assert account_info == "ENTER ACCOUNT INFORMATION"

driver.find_element(By.CSS_SELECTOR, "input[id='id_gender1']").click()
driver.find_element(By.XPATH,"//input[@data-qa='password']").send_keys(password)

Select(driver.find_element(By.ID,"days")).select_by_value("10")
month_dropdown = driver.find_element(By.ID,"months")
month_obj = Select(month_dropdown)
month_obj.select_by_value("9")
Select(driver.find_element(By.ID,"years")).select_by_value("1998")

driver.find_element(By.NAME,"newsletter").click()
driver.find_element(By.NAME,"optin").click()

driver.find_element(By.ID,"first_name").send_keys("Abdur")
driver.find_element(By.ID,"last_name").send_keys("Rehman")
driver.find_element(By.ID,"company").send_keys("AR Ltd")
driver.find_element(By.ID,"address1").send_keys("abd123 PO 123")
Select(driver.find_element(By.ID,"country")).select_by_index(1)
driver.find_element(By.ID,"state").send_keys("California")
driver.find_element(By.ID,"city").send_keys("California")
driver.find_element(By.ID,"zipcode").send_keys("CA123")
driver.find_element(By.ID,"mobile_number").send_keys("090078601")
driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()

account_created = driver.find_element(By.XPATH,"//h2[starts-with(.,'Account Created!')]").text
print(account_created)
assert account_created == "ACCOUNT CREATED!"

driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
account_logged = driver.find_element(By.XPATH,"//ul//a[starts-with(.,' Logged')]").text
print(account_logged)
assert account_logged == "Logged in as Abdul-ur-Rehman"
driver.find_element(By.LINK_TEXT,"Delete Account").click()
account_deleted = driver.find_element(By.XPATH,"//h2[starts-with(.,'Acc')]").text
print(account_deleted)
assert account_deleted == "ACCOUNT DELETED!"
driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()
driver.close()