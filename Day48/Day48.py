import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
item_ids = [item.get_attribute("id") for item in driver.find_elements(By.CSS_SELECTOR, "#store div")]

timeout = time.time() + 1
end_time = time.time() + 60

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        for price in all_prices:
            text = price.text
            if "-" in text:
                try:
                    cost = int(text.split("-")[1].strip().replace(",", ""))
                    item_prices.append(cost)
                except ValueError:
                    continue

        upgrades = {cost: id_ for cost, id_ in zip(item_prices, item_ids)}

        try:
            money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        except ValueError:
            money = 0

        affordable = {cost: id_ for cost, id_ in upgrades.items() if money >= cost}

        if affordable:
            best_upgrade = affordable[max(affordable)]
            driver.find_element(By.ID, best_upgrade).click()

        timeout = time.time() + 5

    if time.time() > end_time:
        print(driver.find_element(By.ID, "cps").text.title())
        break

driver.quit()
