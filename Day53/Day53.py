import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Constants
HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM_URL = "YOUR_GOOGLE_FORM_LINK_HERE"

print("Day 53 - 100 Days of Code.")
print("Welcome to Data Entry Job Automation - Capstone.")


# Helper Functions
def fetch_property_data():
    """Fetches property links, addresses, and prices from the Zillow clone website."""
    response = requests.get(ZILLOW_URL, headers=HEADER)
    soup = BeautifulSoup(response.text, features="html.parser")

    links = [link["href"] for link in soup.select(".StyledPropertyCardDataWrapper a")]
    addresses = [address.get_text().replace(__old=" | ", __new=" ").strip() for address in
                 soup.select(".StyledPropertyCardDataWrapper address")]
    prices = [price.get_text().replace(__old="/mo", __new="").split("+")[0] for price in
              soup.select(".PropertyCardWrapper span") if "$" in price.text]

    return links, addresses, prices


def fill_google_form(driver, address, price, link):
    """Fills a single entry in the Google Form."""
    try:
        address_field = driver.find_element(by=By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                                  '1]/div/div[1]/input')
        price_field = driver.find_element(by=By.XPATH,
                                          value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                '1]/div/div[1]/input')
        link_field = driver.find_element(by=By.XPATH,
                                         value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                               '1]/div/div[1]/input')
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

        address_field.send_keys(address)
        price_field.send_keys(price)
        link_field.send_keys(link)
        submit_button.click()
        time.sleep(1)
    except Exception as e:
        print(f"Error filling form: {e}")


# Main Script
def main():
    # Part 1: Scrape property data
    all_links, all_addresses, all_prices = fetch_property_data()
    print(f"Found {len(all_links)} properties.")

    # Part 2: Fill Google Form
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    for address, price, link in zip(all_addresses, all_prices, all_links):
        driver.get(GOOGLE_FORM_URL)
        time.sleep(2)
        fill_google_form(driver, address, price, link)

    driver.quit()


if __name__ == "__main__":
    main()
