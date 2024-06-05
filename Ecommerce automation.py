from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

from test import driver

fake_data = Faker()
invalid_username = fake_data.user_name()
invalid_password = fake_data.password()
class Authentication():
    def auth(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
#When user enter invalid username and invalid password
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys(invalid_username)
        driver.find_element(By.XPATH,"(//input[@id='password'])[1]").send_keys(invalid_password)
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        #time.sleep(3)
        error = driver.find_element(By.XPATH,"//h3[@data-test='error']")
        error_message = error.text
        print(error_message)
        driver.refresh()
#When user enter invalid username , valid password
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(invalid_username)
        driver.find_element(By.XPATH, "(//input[@id='password'])[1]").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        #time.sleep(3)
        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        error_message = error.text
        print(error_message)
        driver.refresh()
#When user enter valid username , invalid password
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "(//input[@id='password'])[1]").send_keys(invalid_password)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        #time.sleep(3)
        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        error_message = error.text
        print(error_message)
        driver.refresh()
#When user enters valid username and valid password
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH, "(//input[@id='password'])[1]").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        page_title = driver.title
        print(page_title)
        #time.sleep(3)
#Verifying the search functionality
        driver.get("https://saucelabs.com/")
        driver.find_element(By.XPATH,"//img[@src='/images/search.svg']").click()
        driver.find_element(By.XPATH,"//input[@id='search']").send_keys("Sauce")
        driver.find_element(By.PARTIAL_LINK_TEXT,"Sauce").click()
        #time.sleep(3)

auth1 = Authentication()
auth1.auth()
