from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


email = 'abdulurrehman@abcd.com'
name = 'Abdul-ur-Rehman'
password = 'abc123'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

actions = ActionChains(driver)

driver.get('http://automationexercise.com')

driver.find_element(By.XPATH, "//a[@href='/products']").click()

all_products = driver.find_element(By.XPATH, "//h2[starts-with(.,'All')]").text
print(all_products)
assert "ALL PRODUCTS" == all_products

driver.find_element(By.ID,"search_product").send_keys("Blue")
driver.find_element(By.ID,"submit_search").click()

searched_products = driver.find_element(By.XPATH,"//h2[starts-with(.,'Searched')]").text
print(searched_products)
assert "SEARCHED PRODUCTS" == searched_products

#products_container = driver.find_elements(By.XPATH,"//div//img[contains(@src,'picture')]")
products_container = driver.find_elements(By.XPATH,"//div[@class='productinfo text-center']")
print(products_container)
print(len(products_container))

all_products_titles = []

for container in products_container:

    product_title = container.find_element(By.XPATH, ".//p[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'blue')]").text
    all_products_titles.append(product_title)


    driver.execute_script("arguments[0].scrollIntoView(true);", container)
    actions.move_to_element(container).perform()
    add_to_cart = container.find_element(By.XPATH, ".//a[contains(text(),'Add to cart')]")
    WebDriverWait(driver,5).until(EC.element_to_be_clickable(add_to_cart))
    driver.execute_script("arguments[0].click();", add_to_cart)

    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//h4[contains(text(),'Added!')]")))
    driver.find_element(By.XPATH, "//button[text()='Continue Shopping']").click()


print(all_products_titles)

cart_link = driver.find_element(By.XPATH, "//a[@href='/view_cart']")
driver.execute_script("arguments[0].scrollIntoView(true);", cart_link)
cart_link.click()


cart_items = driver.find_elements(By.XPATH, "//tr/td[@class='cart_description']")
cart_list = []

for item in cart_items:

    item_title = item.find_element(By.XPATH, ".//h4").text
    cart_list.append(item_title)

print(cart_list)
assert cart_list == all_products_titles

driver.find_element(By.XPATH, "//a[@href='/login']").click()
driver.find_element(By.XPATH,"//input[@data-qa='login-email']").send_keys(email)
driver.find_element(By.XPATH,"//input[@data-qa='login-password']").send_keys(password)

driver.find_element(By.XPATH,"//button[@data-qa='login-button']").click()


driver.find_element(By.XPATH,"//a[@href='/view_cart']").click()

items_as_loggedin = driver.find_elements(By.XPATH, "//tr/td[@class='cart_description']")
loggedin_cart_itmes = []

for item in items_as_loggedin:

    item_title = item.find_element(By.XPATH, ".//h4").text
    loggedin_cart_itmes.append(item_title)


assert loggedin_cart_itmes == cart_list

driver.find_element(By.XPATH, "//a[@href='/logout']").click()

driver.quit()

