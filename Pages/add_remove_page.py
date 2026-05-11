from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class AddRemovePage:
    URL = "https://the-internet.herokuapp.com/"
    ADD_REMOVE_PAGE_LINK = (By.CSS_SELECTOR,"a[href='/add_remove_elements/']")
    ADD_BUTTON = (By.CSS_SELECTOR,"button[onclick='addElement()']")
    DELETE_BUTTONS = (By.CSS_SELECTOR,"button[onclick='deleteElement()']")   
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
    
    def open(self):
        self.driver.get(self.URL)
    
    def open_add_remove_page(self):
        self.wait.until(EC.presence_of_element_located(self.ADD_REMOVE_PAGE_LINK))
        add_remove_link = self.driver.find_element(*self.ADD_REMOVE_PAGE_LINK)
        add_remove_link.click()
    
    def ajout_element(self):
        self.wait.until(EC.presence_of_element_located(self.ADD_BUTTON))
        add_click = self.driver.find_element(*self.ADD_BUTTON)
        add_click.click()
    
    def suppression_element(self):
        self.wait.until(EC.presence_of_element_located(self.DELETE_BUTTONS))
        delete_click = self.driver.find_elements(*self.DELETE_BUTTONS)
        delete_click[0].click()