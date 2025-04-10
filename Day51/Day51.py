import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
PROMISED_DOWN = 150
PROMISED_UP = 75
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """Fetches internet speed using Speedtest.net."""
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".start-button a").click()
        time.sleep(60)
        self.up = self._get_speed('div[2]/div/div[2]/span')
        self.down = self._get_speed('div[3]/div/div[2]/span')

    def _get_speed(self, relative_xpath):
        """Helper to extract speed values."""
        base_path = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/'
        return self.driver.find_element(By.XPATH, base_path + relative_xpath).text

    def tweet_at_provider(self):
        """Logs into Twitter and tweets about the internet speed."""
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        self._login_to_twitter()
        time.sleep(5)
        self._compose_and_send_tweet()
        self.driver.quit()

    def _login_to_twitter(self):
        """Helper to log into Twitter."""
        email = self.driver.find_element(By.XPATH, '//input[@name="session[username_or_email]"]')
        password = self.driver.find_element(By.XPATH, '//input[@name="session[password]"]')
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

    def _compose_and_send_tweet(self):
        """Helper to compose and send a tweet."""
        tweet = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up "
                 f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_box = self.driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Tweet text"]')
        tweet_box.send_keys(tweet)
        self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]').click()


# Run the bot
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
