from selenium import webdriver
from selenium.webdriver.common.by import By

email = 'abdulurrehman@xyz.com'
name = 'Abdul-ur-Rehman'
password = 'abc123'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://automationexercise.com/")

driver.find_element(By.XPATH, "//a[@href='/login']").click()
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys(email)
driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys(password)

driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()

error_text = driver.find_element(By.XPATH,"//p[starts-with(.,'Your')]").text

print(error_text)

assert error_text == "Your email or password is incorrect!"

driver.close()

