from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestFrontend(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:5000')

    def test_navigation(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, 'Dashboard').click()
        self.assertIn('Dashboard', driver.page_source)

    def test_login_validation(self):
        driver = self.driver
        driver.find_element(By.NAME, 'email').send_keys('wrongemail@example.com')
        driver.find_element(By.NAME, 'password').send_keys('wrongpassword')
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        self.assertIn('Invalid credentials', driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
