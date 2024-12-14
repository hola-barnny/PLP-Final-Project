from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestUIFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:5000")

    def test_login_flow(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

        # Fill login form
        driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
        driver.find_element(By.NAME, "password").send_keys("password123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Validate redirect
        WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
        self.assertIn("Dashboard", driver.page_source)

    def test_messaging_flow(self):
        driver = self.driver
        self.test_login_flow()

        # Navigate to messaging page
        driver.find_element(By.LINK_TEXT, "Messaging").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "message-input")))

        # Send a message
        driver.find_element(By.ID, "message-input").send_keys("Hello, Teacher!")
        driver.find_element(By.ID, "send-button").click()

        # Validate message sent
        messages = driver.find_elements(By.CLASS_NAME, "message")
        self.assertIn("Hello, Teacher!", [msg.text for msg in messages])

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
