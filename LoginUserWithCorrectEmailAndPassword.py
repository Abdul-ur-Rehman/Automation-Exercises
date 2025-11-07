import time

from selenium import webdriver
from selenium.webdriver.common.by import By

email = 'abdulurrehman@abcd.com'
name = 'Abdul-ur-Rehman'
password = 'abc123'


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://automationexercise.com/")

driver.find_element(By.LINK_TEXT,"Signup / Login").click()
account_login = driver.find_element(By.XPATH,"//h2[starts-with(.,'Login')]").text
print(account_login)
assert account_login == "Login to your account"

driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys(email)
driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys(password)
driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()
account_logged = driver.find_element(By.XPATH,"//ul//a[starts-with(.,' Logged')]").text
print(account_logged)
assert account_logged == "Logged in as Abdul-ur-Rehman"

driver.find_element(By.LINK_TEXT,"Logout").click()

driver.close()

