import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\development\chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3483364304&f_AL=true&geoId=101620260&keywords=python&location=Israel&refresh=true")

time.sleep(3)

email = "omrirahmani1001@gmail.com"
password = "936855275388"
phone = "+972526453661"
#Signing in
first_sign_in = driver.find_element(by="css selector", value=".btn-secondary-emphasis")
first_sign_in.click()
# Wait for page to load
time.sleep(3)
email_field = driver.find_element(by="id", value="username")
email_field.send_keys(email)
password_field = driver.find_element(by="id", value="password")
password_field.send_keys(password)
sign_in_button = driver.find_element(by="xpath", value="//*[@id='organic-div']/form/div[3]/button")
sign_in_button.click()

#Wait for page to load and solve captcha
time.sleep(20)

def apply():
    easy_apply = driver.find_element(by="css selector", value=".jobs-apply-button--top-card")
    easy_apply.click()
    time.sleep(5)
    # Fill in application fields
    phone_field = driver.find_element(by="css selector", value='.artdeco-text-input--input')
    if phone_field.get_attribute("value") == "":
        phone_field.send_keys(phone)
    next_button = driver.find_element(by="css selector", value=".artdeco-button--primary span")
    # Check if button is submit or next
    if next_button.text != "Next":
        submit = driver.find_element(by="css selector", value=".artdeco-button--primary")
        submit.click()
        time.sleep(5)
    else:
        time.sleep(5)
        #check_button = driver.find_element(by="css selector", value=".artdeco-button")
        next_button.click()
        time.sleep(10)
        options = driver.find_elements(by="css selector", value=".artdeco-button--tertiary span")
        for op in options:
            if op.text == "Choose":
                op.click()
                break
        time.sleep(3)
        next_button = driver.find_element(by="css selector", value=".artdeco-button--primary")
        next_button.click()
        time.sleep(3)
        check_button = driver.find_element(by="css selector", value=".artdeco-button--primary span")
        if check_button.text != "Next" and check_button.text != "Review":
            submit = driver.find_element(by="css selector", value=".artdeco-button--primary")
            submit.click()
            time.sleep(3)
        else:
            close = driver.find_element(by="css selector", value=".artdeco-modal__dismiss")
            close.click()
            time.sleep(2)
            discard = driver.find_element(by="css selector", value=".artdeco-modal__confirm-dialog-btn")
            discard.click()
            time.sleep(2)

# Store job listings on page to click on for applying
job_listings = driver.find_elements(by="css selector", value=".jobs-search-results__list-item")
for job in job_listings:
    time.sleep(3)
    try:
        job.click()
    except:
        pass
    time.sleep(3)
    apply()
driver.quit()

apply()
while True:
    pass




