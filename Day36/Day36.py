import smtplib
from datetime import datetime as dt, timedelta as td

import requests

send_email = False
ZERO = 0
ONE = 1
TWO = 2
appender = ""
whitespace = " "
new_line_character = "\n"
tesla_stock_details = []

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_price_api_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"
my_email = "ask@gmail.com"
my_email_password = "************"
# Can be obtained here: https://www.alphavantage.co/support/#api-key
stock_price_api_key = "************"
# Can be obtained here: https://newsapi.org/
news_api_key = "************"

stock_price_api_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": stock_price_api_key
}

news_api_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api_key
}

current_day = dt.now().strftime("%A")
if current_day == "Monday":
    yesterday_offset_value = TWO
    day_before_yesterday_offset_value = TWO
elif current_day == "Tuesday":
    yesterday_offset_value = ZERO
    day_before_yesterday_offset_value = TWO
else:
    yesterday_offset_value = ZERO
    day_before_yesterday_offset_value = ZERO

yesterday = str(dt.now() - td(ONE + yesterday_offset_value))[:10]
day_before_yesterday = str(dt.now() - td(TWO + day_before_yesterday_offset_value))[:10]
stock_price = requests.get(url=stock_price_api_url, params=stock_price_api_parameters)
stock_price.raise_for_status()
stock_price = stock_price.json()["Time Series (Daily)"]
# stock_price = demo["Time Series (Daily)"]
yesterday_stock_price = float(stock_price[yesterday]['4. close'])
day_before_yesterday_stock_price = float(stock_price[day_before_yesterday]['4. close'])
percentage_change_in_stock_price = ((day_before_yesterday_stock_price - yesterday_stock_price) * 100 /
                                    day_before_yesterday_stock_price)
if percentage_change_in_stock_price > 5:
    appender = "INCREASE!"
    send_email = True
elif percentage_change_in_stock_price < -5:
    appender = "DECREASE!"
    send_email = True
appender += (whitespace + COMPANY_NAME + whitespace + str(round(percentage_change_in_stock_price, TWO))
             + "%" + new_line_character)

news_details = requests.get(url=news_url, params=news_api_parameters)
news_details.raise_for_status()
news_details = news_details.json()["articles"][:3]
for index in range(len(news_details)):
    news = ("Title: " + str(news_details[index]["title"].encode('ascii', 'ignore').decode('ascii')) + new_line_character
            + "Description: " + str(news_details[index]["description"].encode('ascii', 'ignore').decode('ascii')))

    tesla_stock_details.append("Subject: " + appender + new_line_character * TWO + news)

if send_email:
    print("Steep changes in stock price observed. Email will be sent.")
    with smtplib.SMTP("SMTP.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_email_password)
        for iterator in range(3):
            try:
                connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=tesla_stock_details[iterator])
            except UnicodeDecodeError:
                pass
else:
    print("Major changes in stock price not seen. No email will be sent.")
