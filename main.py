import unittest
from selenium import webdriver
from bs4 import BeautifulSoup


class seleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def testEle(self):
        driver = self.driver
        driver.get('http://www.douyu.com/directory/all')
	print(driver.title.encode('utf8'))

    def tearDown(self):
        print 'down'

if __name__ == "__main__":
    unittest.main()
