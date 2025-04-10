import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
SIMILAR_ACCOUNT = "python"
USERNAME = os.getenv("YOUR_USERNAME")
PASSWORD = os.getenv("YOUR_PASSWORD")

print("Day 52 - 100 Days of Code.")
print("Welcome to Instagram Follower Bot.")


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        """Logs into Instagram."""
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)

        # Handle cookie warning if present
        cookie_warning = self._find_element(by=By.XPATH,
                                            value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div["
                                                  "2]/div/button[2]")
        if cookie_warning:
            cookie_warning.click()

        self._find_element(By.NAME, "username").send_keys(USERNAME)
        password_field = self._find_element(by=By.NAME, value="password")
        password_field.send_keys(PASSWORD)
        time.sleep(2)
        password_field.send_keys(Keys.ENTER)

        time.sleep(4)
        # Handle prompts
        self._click_if_present(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        time.sleep(3)
        self._click_if_present(by=By.XPATH, value="//button[contains(text(), 'Not Now')]")

    def find_followers(self):
        """Navigates to the followers list of a similar account."""
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(8)

        modal = self._find_element(by=By.XPATH,
                                   value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        for _ in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        """Follows users from the followers list."""
        buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value='._aano button')
        for button in buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                self._click_if_present(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")

    def _find_element(self, by, value):
        """Helper to find an element."""
        return self.driver.find_element(by=by, value=value)

    def _click_if_present(self, by, value):
        """Helper to click an element if it exists."""
        element = self.driver.find_elements(by=by, value=value)
        if element:
            element[0].click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
