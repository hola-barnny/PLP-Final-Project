from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestWebUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5000')

    def test_login_button(self):
        driver = self.driver
        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        self.assertTrue(login_button.is_displayed())

    def test_message_input_field(self):
        driver = self.driver
        message_field = driver.find_element(By.ID, 'message-input')
        self.assertTrue(message_field.is_displayed())

    def test_dashboard_navigation(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, 'Dashboard').click()
        self.assertIn('Dashboard', driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
