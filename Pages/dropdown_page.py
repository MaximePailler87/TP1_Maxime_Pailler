from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/"
    DROPDOWN_PAGE_LINK = (By.CSS_SELECTOR,"a[href='/dropdown']")
    DROPDOWN_LIST = (By.ID, "dropdown")    
    
    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)
    
    def open(self):
        self.driver.get(self.URL)
    
    def open_dropdown_page(self):
        self.wait.until(EC.presence_of_element_located(self.DROPDOWN_PAGE_LINK))
        dropdown_link = self.driver.find_element(*self.DROPDOWN_PAGE_LINK)
        dropdown_link.click()
    
    def select(self, option):
        self.wait.until(EC.presence_of_element_located(self.DROPDOWN_LIST))
        main_dropdown = self.driver.find_element(*self.DROPDOWN_LIST)
        dropdown = Select(main_dropdown)
        dropdown.select_by_visible_text(option)
        return dropdown.first_selected_option.text
        
    