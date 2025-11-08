import time
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


email = 'abdulurrehman@abc.com'
name = 'Abdul-ur-Rehman'
password = 'abc123'


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://automationexercise.com/")

actions = ActionChains(driver)

home_page_text = driver.find_element(By.XPATH,"//h2[starts-with(.,'Full')]").text
print(home_page_text)
assert home_page_text == "Full-Fledged practice website for Automation Engineers"

product_card = driver.find_element(By.XPATH,"(//div[@class='col-sm-4'])[2]")
driver.execute_script("arguments[0].scrollIntoView(true);", product_card)

actions.move_to_element(product_card).perform()
product_name = product_card.find_element(By.XPATH,".//p").text
print(product_name)
add_cart = product_card.find_element(By.XPATH,".//a[contains(@class,'add-to-cart')]")
driver.execute_script("arguments[0].click();",add_cart)

WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Continue Shopping')]"))).click()

driver.find_element(By.XPATH,"//div/ul/li/a[@href='/view_cart']").click()

cart_page_text = driver.find_element(By.XPATH,"//li[contains(.,'Shopping Cart')]").text
print(cart_page_text)
assert "Shopping Cart" == cart_page_text

driver.find_element(By.XPATH,"//div/a[contains(@class,'check_out')]").click()
driver.find_element(By.XPATH,"//div//p//a[@href='/login']").click()

driver.find_element(By.XPATH,"//input[@data-qa='signup-name']").send_keys(name)
driver.find_element(By.XPATH,"//input[@data-qa='signup-email']").send_keys(email)
driver.find_element(By.XPATH,"//button[@data-qa='signup-button']").click()

account_registration_text = driver.find_element(By.XPATH,"//h2[contains(.,'Enter')]").text
print(account_registration_text)
assert account_registration_text == "ENTER ACCOUNT INFORMATION"

driver.find_element(By.XPATH,"//input[@id='id_gender1']").click()
driver.find_element(By.ID,"password").send_keys(password)

Select(driver.find_element(By.ID,"days")).select_by_value("10")
Select(driver.find_element(By.ID,"months")).select_by_value("9")
Select(driver.find_element(By.ID,"years")).select_by_value("1998")

driver.find_element(By.ID,"newsletter").click()
driver.find_element(By.ID,"optin").click()

driver.find_element(By.ID,"first_name").send_keys("Abdur")
driver.find_element(By.ID,"last_name").send_keys("Rehman")
driver.find_element(By.ID,"company").send_keys("AR Ltd.")
driver.find_element(By.ID,"address1").send_keys("ABC PO 123")
Select(driver.find_element(By.ID,"country")).select_by_index(1)
driver.find_element(By.ID,"state").send_keys("California")
driver.find_element(By.ID,"city").send_keys("California")
driver.find_element(By.ID,"zipcode").send_keys("CA 123")
driver.find_element(By.ID,"mobile_number").send_keys("090078601")
driver.find_element(By.XPATH,"//button[@data-qa='create-account']").click()

account_creation_text = driver.find_element(By.XPATH,"//p[contains(.,'Cong')]").text
print(account_creation_text)
assert "Congratulations" in account_creation_text
driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()

loggedin_text = driver.find_element(By.XPATH,"//a[contains(.,'Logg')]").text
print(loggedin_text)
assert loggedin_text == "Logged in as Abdul-ur-Rehman"

driver.find_element(By.XPATH,"//div/ul/li/a[@href='/view_cart']").click()
driver.find_element(By.XPATH,"//div/a[contains(@class,'check_out')]").click()

home_address = driver.find_element(By.XPATH,"(//li[contains(@class,'address_address1')])[2]").text
city_address = driver.find_element(By.XPATH,"//li[contains(@class,'address_city')]").text
country_address = driver.find_element(By.XPATH,"//li[contains(@class,'address_country_name')]").text
print(home_address)
print(city_address)
print(country_address)

assert home_address == "ABC PO 123"
assert city_address == "California California CA 123"
assert country_address == "United States"

product_name_cart = driver.find_element(By.XPATH,"//h4/a").text

assert product_name_cart == product_name

driver.find_element(By.XPATH,"//textarea[@name='message']").send_keys("My First Order.")
driver.find_element(By.XPATH,"//a[text()='Place Order']").click()

driver.find_element(By.NAME,"name_on_card").send_keys(name)
driver.find_element(By.NAME,"card_number").send_keys("1234123412341234")
driver.find_element(By.NAME,"cvc").send_keys("321")
driver.find_element(By.NAME,"expiry_month").send_keys("09")
driver.find_element(By.NAME,"expiry_year").send_keys("2030")
driver.find_element(By.CSS_SELECTOR,"#submit").click()


order_placement = driver.find_element(By.XPATH,"//p[contains(.,'Cong')]").text
print(order_placement)
assert "Congratulations" in order_placement

driver.find_element(By.XPATH,"//a[@href='/download_invoice/500']").click()

time.sleep(3)

invoice = open(r"C:\Users\sg\Downloads\invoice.txt", "r")
line = invoice.readline()
print(line)

assert "Thank you" in line
invoice.close()
os.remove(r"C:\Users\sg\Downloads\invoice.txt")

driver.find_element(By.XPATH,"//a[@data-qa='continue-button']").click()

driver.find_element(By.XPATH,"//a[@href='/delete_account']").click()
account_deleted = driver.find_element(By.XPATH,"//h2").text
print(account_deleted)
assert "ACCOUNT DELETED!" == account_deleted

driver.quit()