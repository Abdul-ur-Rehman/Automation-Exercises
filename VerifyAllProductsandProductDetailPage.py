from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver =webdriver.Chrome(options=options)


driver.get("https://automationexercise.com/")

home_verification = driver.find_element(By.XPATH,"//h1[starts-with(.,'Auto')]").text
assert home_verification == "AutomationExercise"

driver.find_element(By.XPATH,"//a[@href='/products']").click()

all_products = driver.find_element(By.XPATH,"//h2[text()='All Products']").text
print(all_products)
assert all_products == "ALL PRODUCTS"

driver.find_element(By.XPATH,"//a[@href='/product_details/1']").click()

product_title = driver.find_element(By.XPATH,"//h2[contains(.,'Blue Top')]").text
product_category = driver.find_element(By.XPATH,"//p[contains(.,'Category')]").text
product_price = driver.find_element(By.XPATH,"//span[starts-with(.,'Rs')]").text
product_availability = driver.find_element(By.XPATH,"//p[starts-with(.,'Avail')]").text
product_condition = driver.find_element(By.XPATH,"//p[starts-with(.,'Condition')]").text
product_brand = driver.find_element(By.XPATH,"//p[starts-with(.,'Brand')]").text

print(product_title)
print(product_category)
print(product_price)
print(product_availability)
print(product_condition)
print(product_brand)

assert product_title == "Blue Top"
assert product_category == "Category: Women > Tops"
assert product_price == "Rs. 500"
assert product_availability == "Availability: In Stock"
assert product_condition == "Condition: New"
assert product_brand == "Brand: Polo"

driver.close()
