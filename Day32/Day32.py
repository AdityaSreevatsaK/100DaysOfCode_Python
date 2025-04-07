import datetime as dt
import smtplib
from random import randint

import pandas as pd

my_email = "ask@gmail.com"
my_password = "************"
EMPTY_STRING = ""
randomised_email = EMPTY_STRING
recipient_name = EMPTY_STRING
recipient_email = EMPTY_STRING
send_email_flag = False

print("Day 32 - 100 Days of Code.")
print("Welcome to Automated Birthday Wisher!")

CURRENT_DAY = dt.datetime.now().day
CURRENT_MONTH = dt.datetime.now().month

birthday_data = pd.read_csv("birthdays.csv")
for index, row in birthday_data.iterrows():
    if row["day"] == CURRENT_DAY and row["month"] == CURRENT_MONTH:
        send_email_flag = True
        recipient_name = row["name"]
        recipient_email = row["email"]

if send_email_flag:
    with open(file="letter_templates/letter_" + str(randint(1, 3)) + ".txt", mode="r") as happy_birthday_email:
        for line in happy_birthday_email:
            randomised_email += line

    randomised_email = "Subject:Happy Birthday!\n\n" + randomised_email.replace("[NAME]", recipient_name)
    print(randomised_email)
    with smtplib.SMTP("SMTP.gmail.com") as connection:
        # connection.starttls() - Starts the transport layer security.
        # Encrypts your email such that no one in between can intercept and read it.
        connection.starttls()
        connection.login(user=my_email, password=my_password)  # Login using your app creds.
        connection.sendmail(from_addr=my_email, to_addrs=recipient_email, msg=randomised_email)
