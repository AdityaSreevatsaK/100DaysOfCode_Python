import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()
linkedin_email = os.getenv('LINKEDIN_EMAIL')
linkedin_password = os.getenv('LINKEDIN_PASSWORD')
phone_number = os.getenv('PHONE_NUMBER')
wait_time = 2
listings_viewed = 0
jobs_applied_to = 0
skipped_due_to_complexity = 0

linkedin_login_page = "https://www.linkedin.com/login"

linkedin_job_application_url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491" \
                               "&keywords=python%20developer&location=Bengaluru%2C%20Karnataka%2C%20India" \
                               "&redirect=false&position=1&pageNum=0"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

print("Day  - 100 Days of Code.")
print("Welcome to Automating Job Applications on LinkedIn.")


def abort_application():
    """
    Aborts the current job application process on LinkedIn by closing the application modal
    and discarding any unsaved changes.

    Steps:
    1. Locate and click the close button to dismiss the application modal.
    2. Wait for 2 seconds to ensure the modal is dismissed.
    3. Locate and click the discard button to confirm discarding the application.
    """
    close_application_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_application_button.click()

    discard_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")
    discard_button.click()


driver.get(linkedin_login_page)
email_address_field = driver.find_element(by=By.ID, value='username')
password_field = driver.find_element(by=By.ID, value='password')
email_address_field.send_keys(linkedin_email)
password_field.send_keys(linkedin_password)
sign_in_button = driver.find_element(by=By.XPATH, value='//button[@type="submit"]')
sign_in_button.click()
print("Sign in complete.")
time.sleep(wait_time)

driver.get(linkedin_job_application_url)
print("LinkedIn Jobs page opened.")
time.sleep(wait_time)

# Get Listings
time.sleep(wait_time)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listings_viewed += 1
    listing.click()
    time.sleep(wait_time)
    try:
        # Ensure job is not already applied for.
        applied_list = driver.find_elements(by=By.ID, value='jobs-apply-see-application-link')
        if len(applied_list) > 0:
            continue

        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        # Find an <input> element where the id contains phoneNumber
        time.sleep(wait_time)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(Keys.CONTROL + 'A')
            phone.send_keys(Keys.BACKSPACE)
            phone.send_keys(phone_number)

        # Check the Submit Button
        print("Checking if application can be submitted.")
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.text.lower() in ("next", "review"):
            print("Complex application, skipped.")
            skipped_due_to_complexity += 1
            abort_application()
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            jobs_applied_to += 1
            submit_button.click()

        time.sleep(wait_time)

        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue

time.sleep(wait_time)
driver.quit()
