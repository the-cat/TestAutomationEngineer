import unittest
import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGoogleCalendar(unittest.TestCase):

    """
    This is a test class for testing google-calendar using selenium
    """

    def test_createEventButton(self):
        driver = webdriver.Chrome()
        driver.get('http://calendar.google.com')
        elem_username = driver.find_element_by_name('identifier')
        elem_username.clear()
        elem_username.send_keys(os.environ['GOOGLE_USERNAME'])
        driver.find_element_by_id('identifierNext').click()
        time.sleep(5)
        elem_password = driver.find_element_by_name('password')
        elem_password.clear()
        elem_password.send_keys(os.environ['GOOGLE_PASSWORD'])
        driver.find_element_by_id('passwordNext').click()
        time.sleep(5)
        driver.find_element_by_css_selector('#createEventButtonContainer > div > div.goog-inline-block.goog-imageless-button.goog-imageless-button-collapse-left.qnb-qab').click()
        elem_qa_event_name = driver.find_element_by_id(':x.textarea')
        elem_qa_event_name.clear()
        elem_qa_event_name.send_keys('Dinner at the Ritz')
        driver.find_element_by_css_selector('body > div.qab-container.gcal-popup > div').click()
        time.sleep(5)
        driver.find_element_by_css_selector(r'#\3a 1p\2e save_top > div').click()
        time.sleep(5)
        driver.close()

if __name__ == '__main__':
    unittest.main()