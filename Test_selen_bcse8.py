import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:/chromedriver')
driver.get("http://www.bcse.by/en")
self.assertIn("Bcse", driver.title)
elem = driver.find_element_by_name("market")
elem.send_keys("indicators")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
    
if __name__ == "__main__":
    unittest.main()