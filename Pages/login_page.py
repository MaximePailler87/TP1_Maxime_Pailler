from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://the-internet.herokuapp.com/"
    #LOGIN_PAGE_LINK = (By.CSS_SELECTOR,"a[href='/login']")
    LOGIN_PAGE_LINK = (By.XPATH,"//a[@href='/login']")
    USER_INPUT = (By.ID, "username")
    PWD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class='radius']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR,"a[href='/logout']")
    MESSAGE_FLASH = (By.ID, "flash")
    
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self):
        self.driver.get(self.URL)
    
    def open_login_page(self):
        self.wait.until(EC.presence_of_element_located(self.LOGIN_PAGE_LINK))
        login_link = self.driver.find_element(*self.LOGIN_PAGE_LINK)
        login_link.click()
    
    def input_username(self,query):
        user_field = self.driver.find_element(*self.USER_INPUT)
        user_field.clear()
        user_field.send_keys(query)
    
    def input_password(self,query):
        pwd_field = self.driver.find_element(*self.PWD_INPUT)
        pwd_field.clear()
        pwd_field.send_keys(query)
    
    def click_login(self):
        self.wait.until(EC.presence_of_element_located(self.LOGIN_BUTTON))
        login_click = self.driver.find_element(*self.LOGIN_BUTTON)
        login_click.click()
    
    def click_logout(self):
        self.wait.until(EC.presence_of_element_located(self.LOGOUT_BUTTON))
        logout_click = self.driver.find_element(*self.LOGOUT_BUTTON)
        logout_click.click()
    
    def verif_message(self):
        self.wait.until(EC.presence_of_element_located(self.MESSAGE_FLASH))
        output = self.driver.find_element(*self.MESSAGE_FLASH)
        return output.text
    
    