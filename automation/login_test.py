import time
import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument('--log-level=3')

    correct_email = "zelf_test@yopmail.com"
    correct_password = "Aneeka12345"

    incorrect_email = "dummy@example.com"
    incorrect_password = "12345"

    inactive_email = "tabassum.aneeka+test1@gmail.com"
    password_for_inactive_user = "123456aA@"

    def setUp(self):
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://zelf-hackathon-qa.web.app/")
        self.driver.maximize_window()
        self.wait_for_fully_loaded_page()
        sign_in_button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        sign_in_button.click()
        time.sleep(2)
        sign_in_button.click()
        time.sleep(5)

    def wait_for_fully_loaded_page(self):
        time.sleep(5)

    def test_login_with_wrong_emailaddress(self):
        # Find the email and password input fields
        email_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")

        email_input.send_keys(self.incorrect_email)
        password_input.send_keys(self.correct_password)
        password_input.send_keys(Keys.RETURN)  # Submit form

        # Wait for the page to reload
        self.wait_for_fully_loaded_page()
        error_message = self.driver.find_element(By.ID, "error-element-password")
        self.assertIn("Wrong email or password", error_message.text)

    def test_login_with_wrong_password(self):
        # Find the email and password input fields
        email_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")

        email_input.send_keys(self.correct_email)
        password_input.send_keys(self.incorrect_password)
        password_input.send_keys(Keys.RETURN)  # Submit form

        # Wait for the page to reload
        self.wait_for_fully_loaded_page()
        error_message = self.driver.find_element(By.ID, "error-element-password")
        self.assertIn("Wrong email or password", error_message.text)

    def test_login_successful(self):
        # Find the email and password input fields
        email_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")

        email_input.send_keys(self.correct_email)
        password_input.send_keys(self.correct_password)
        password_input.send_keys(Keys.RETURN)  # Submit form

        # Wait for the page to reload
        self.wait_for_fully_loaded_page()

        current_url = self.driver.current_url
        assert current_url == "https://zelf-hackathon-qa.web.app/feed", f"Unexpected URL: {current_url}"
        page_source = self.driver.page_source
        assert "Daily Progress" in page_source, "Text 'test text' not found on the page"

    def tearDown(self):
        # Teardown method to close the browser after test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()