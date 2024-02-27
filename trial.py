import unittest
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from settings import CHROMEDRIVER_PATH ,WIKIPEDIA_URL
from Page import MainPage

class WikipediaMainPageSearch(unittest.TestCase):
    
    def setUp(self) :
       self.service=Service(executable_path=CHROMEDRIVER_PATH)
       self.driver=webdriver.Chrome(service=self.service)
       self.driver.get(WIKIPEDIA_URL)

    def test_search(self):
        search_text='Python (programming language)' 
        main_page=MainPage(self.driver)
        main_page.search(search_text)
        self.assertEqual(search_text +' - Wikipedia', str(self.driver.title))

    def tearDown(self) :
        self.driver.quit()
        

if __name__=='__main__':
    unittest.main()