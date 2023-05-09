import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserAutomation:
   def _browser(self, url: string):
       options = webdriver.ChromeOptions()
       options.add_experimental_option("detach", True)
       driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
       try:
           driver.get(url)
       except:
           print("Cannot open" + url)


   def open(self, url: string):
       print(url)
       self._browser(url)