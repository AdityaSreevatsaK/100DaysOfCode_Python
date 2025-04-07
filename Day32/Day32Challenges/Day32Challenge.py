import datetime as dt
import smtplib
from random import choice

list_of_motivational_quotes = []
my_email = "ask@gmail.com"
my_password = "************"
TODAY = dt.datetime.now().weekday()

print("Day 32 Challenge - 100 Days of Code.")
print("Welcome to Challenge - Monday Motivational Quotes.")

with open(file="quotes.txt", mode="r") as motivational_quotes:
    for line in motivational_quotes:
        list_of_motivational_quotes.append(line.replace("\n", ""))

with smtplib.SMTP("SMTP.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    if TODAY == 2:
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg="Subject:Wednesday Motivation!\n\n" + choice(list_of_motivational_quotes))
