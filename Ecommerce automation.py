from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker
from test import driver

fake_data = Faker()
invalid_username = fake_data.user_name()
invalid_password = fake_data.password()
class Authentication():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def creds(self,username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "(//input[@id='password'])[1]").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

    def search_query(self,input):
        self.driver.get("https://saucelabs.com/")
        self.driver.find_element(By.XPATH, "//img[@src='/images/search.svg']").click()
        self.driver.find_element(By.XPATH, "//input[@id='search']").send_keys(input)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, input).click()

creds1 = Authentication()
creds1.creds(invalid_username,invalid_password)   #When user enter invalid username and  invalid password
creds1.creds(invalid_username,"secret_sauce") #When user enter invalid username and valid password
creds1.creds("standard_user",invalid_password) #When user enter valid username and invalid password
creds1.creds("standard_user","secret_sauce") #When user enter valid username and valid password
time.sleep(3)

search1 = Authentication()
search1.search_query("Sauce") #searching valid input
search1.search_query(" ") #searching space
search1.search_query("Abnisd") #searching invalid input





