from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_INPUT=(By.CSS_SELECTOR,'input.cdx-text-input__input')
    SEARCH_BUTTON  =(By.CSS_SELECTOR,'button.cdx-button.cdx-search-input__end-button')