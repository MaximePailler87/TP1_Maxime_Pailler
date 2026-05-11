from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DropdownPage:
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