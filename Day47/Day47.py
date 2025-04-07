import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
my_email = os.getenv("EMAIL_ADDRESS")
my_password = os.getenv("EMAIL_PASSWORD")
smtp_address = os.getenv('SMTP_ADDRESS')

apple_macbook_amazon_url = 'https://amzn.in/d/8Hw4GQU'
price_threshold = 300000.0
current_price = 0
email_to_be_sent = f'The price of the Apple Macbook has fallen below the set threshold {price_threshold}. Buy now!'
header_dict = {
    # Get this from https://httpbin.org/headers. Exclude host and X-Amzn-Trace-id.
}

print("Day 47 - Amazon Price Tracker.")
response = requests.get(apple_macbook_amazon_url, headers=header_dict)
response.raise_for_status()
static_page_content = response.text
soup = BeautifulSoup(static_page_content, features='html.parser')
try:
    current_price = float(soup.find(class_='a-price-whole').get_text().replace(',', ''))
    print(f"Today's cost: Rs. {current_price}")
except AttributeError as ae:
    print("Attribute error encountered.", ae)

if current_price < price_threshold:
    # For Gmail SMTP, the port value of 587 indicates STARTTLS (encryption upgrade).
    with smtplib.SMTP(smtp_address, port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Amazon Price Alert!\n\n{email_to_be_sent}\n{apple_macbook_amazon_url}".encode("utf-8")
        )
        print("Email sent. Price has dropped.")
else:
    print("Nope. Still as costly as ever! ;)")
