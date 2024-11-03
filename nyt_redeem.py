import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def enter_field(field, text):
    for c in text:
        field.send_keys(c)
        random_sec_delay = random.uniform(0.1, 0.3)
        time.sleep(random_sec_delay)


def redeem_code(driver, nyt_code):
    driver.get("https://www.nytimes.com/redeem")

    time.sleep(6)

    continue_button = driver.find_element(By.CSS_SELECTOR, 'button.css-j07ljx[data-tpl-type="Button"]')
    continue_button.click()

    code_field = driver.find_element(By.NAME, "code")
    code_field.clear()
    enter_field(code_field, nyt_code)

    time.sleep(2)

    redeem_button = driver.find_element(By.TAG_NAME, 'button')
    redeem_button.click()

def redeem_login(driver, nyt_email, nyt_password):
    email_field = driver.find_element(By.NAME, "email")
    enter_field(email_field, nyt_email)

    time.sleep(2)

    email_login_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-email"]')
    email_login_button.click()
    
    time.sleep(2)

    password_field = driver.find_element(By.NAME, "password")
    enter_field(password_field, nyt_password)

    time.sleep(2)

    login_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="login-button"]')
    login_button.click()

    time.sleep(2)

    page_title_element = driver.find_element(By.CSS_SELECTOR, "h2[data-testid='page-title']")
    
    if page_title_element.text == "It looks like you're already a subscriber":
        driver.quit()

def finish_redeem(driver):
    continue_first = driver.find_element(By.CSS_SELECTOR, '[data-testid="get-started-btn"]')
    continue_first.click()

    time.sleep(2)

    continue_second = driver.find_element(By.CSS_SELECTOR, '[data-testid="welcome-screen-button"]')
    continue_second.click()

    time.sleep(2)

    newsletter_signup_sheet_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="newsletter-signup-sheet-button"]')
    newsletter_signup_sheet_button.click()

    time.sleep(2)

    continue_without_sms = driver.find_element(By.CSS_SELECTOR, '[data-testid="continue-without-sms"]')
    continue_without_sms.click()

def auto_subscribe_nyt():
    load_dotenv()

    nyt_email = os.getenv("NYT_EMAIL")
    nyt_password = os.getenv("NYT_PASSWORD")
    nyt_code = os.getenv("NYT_CODE")

    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    redeem_code(driver, nyt_code)

    time.sleep(5)

    redeem_login(driver, nyt_email, nyt_password)

    time.sleep(5)

    finish_redeem(driver)
    
    time.sleep(5)
    
    driver.quit()