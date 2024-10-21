import smtplib

my_email = "ask@gmail.com"
my_password = "aaaabbbbccccdddd"


def send_email(emails, message, google_flight_link):
    with smtplib.SMTP("SMTP.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        for email in emails:
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
            )
