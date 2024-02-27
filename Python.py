from Locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.common.exceptions import NoSuchElementException
from settings import WAIT_TIME

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,locator_element,locator_string):
        try:
            element= WebDriverWait(self.driver,WAIT_TIME).until(EC.presence_of_element_located((locator_element,locator_string)))
            return element
        except NoSuchElementException as e :
            print(f'No element with {locator_element} of  {locator_string} found ',e)


    def get_text(self,locator_element,locator_string):
        element=self.get_element(locator_element,locator_string)
        return element.get_text

    def enter_text(self,locator_element,locator_string,text):
        return self.get_element(locator_element,locator_string).send_keys(text)
         

    def click_button(self,locator_element,locator_string):
        return self.get_element(locator_element,locator_string).click()

    def get_page_title(self,locator_element,locator_string):
        return self.driver.title

class MainPage(BasePage):
    def search(self,search_string):
        #*MainPageLocators.SEARCH_INPUT means it will send locator type and element string in 2 part
        self.enter_text(*MainPageLocators.SEARCH_INPUT,search_string) 
        self.click_button(*MainPageLocators.SEARCH_BUTTON)
