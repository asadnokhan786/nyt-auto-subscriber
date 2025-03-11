import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from logger_config import logger



def enter_field(field, text):
    logger.debug(f"Entering a {text} into {field}...")
    for c in text:
        field.send_keys(c)
        random_sec_delay = random.uniform(0.1, 0.3)
        time.sleep(random_sec_delay)
    logger.debug(f"Successfully entered {text} into {field}")


def redeem_code(driver, nyt_code):
    logger.debug("Running redeem_code() function...")
    logger.debug("Going to https://www.nytimes.com/redeem...")
    driver.get("https://www.nytimes.com/redeem")

    time.sleep(5)
    try:
        # Use the 'xpath' to locate the button
        continue_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'css-j07ljx') and contains(., 'Continue')]"))
            )

        # Click the button
        continue_button.click()
        logger.debug("The first continue button did pop up and we did click it!")

    except Exception as e:
        logger.debug(f"Error form that first continue button: {e}")

    time.sleep(2)

    code_field = driver.find_element(By.NAME, "code")
    logger.debug(f"Clearing any initial value in {code_field}...")
    code_field.clear()
    enter_field(code_field, nyt_code)

    time.sleep(4)

    logger.debug("Submitting provided code...")
    redeem_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='btn-redeem']")
    redeem_button.click()
    logger.debug("Successfully submitted provided code")
    logger.debug("Successfully ran redeem_code()")

def redeem_login(driver, nyt_email, nyt_password):
    logger.debug("Running redeem_login() function...")
    time.sleep(10)
    email_field = driver.find_element(By.NAME, "email")
    enter_field(email_field, nyt_email)

    time.sleep(4)

    logger.debug("Submitting provided email...")
    email_login_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-email"]')
    email_login_button.click()
    logger.debug("Successfully submitted email")
    
    time.sleep(6)

    password_field = driver.find_element(By.NAME, "password")
    enter_field(password_field, nyt_password)

    time.sleep(2)

    logger.debug("Submitting provided password...")
    login_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="login-button"]')
    login_button.click()
    logger.debug("Successfully submitted provided password")

    time.sleep(2)

    logger.debug("Checking if already subscribed...")
    page_title_element = driver.find_element(By.CSS_SELECTOR, "h2[data-testid='page-title']")
    
    if page_title_element.text == "It looks like you're already a subscriber":
        logger.debug("User is already subscribed, no further action required")
        driver.quit()
    logger.debug("Succesfully ran redeem_login() function")

def finish_redeem(driver):
    logger.debug("Running finish_redeem() function")
    continue_first = driver.find_element(By.CSS_SELECTOR, '[data-testid="get-started-btn"]')
    continue_first.click()
    logger.debug("Checkpoint 1 successfully cleared")

    time.sleep(4)

    continue_second = driver.find_element(By.CSS_SELECTOR, '[data-testid="welcome-screen-button"]')
    continue_second.click()
    logger.debug("Checkpoint 2 successfully cleared")

    time.sleep(7)

    newsletter_signup_sheet_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="newsletter-signup-sheet-button"]')
    newsletter_signup_sheet_button.click()
    logger.debug("Checkpoint 3 successfully cleared")

    time.sleep(8)

    continue_without_sms = driver.find_element(By.CSS_SELECTOR, '[data-testid="continue-without-sms"]')
    continue_without_sms.click()
    logger.debug("Checkpoint 4 successfully cleared")
    logger.debug("Successfully ran finish_redeem() function")

def auto_subscribe_nyt():
    logger.debug("Running auto_subscribe_nyt() function...")
    logger.debug("Loading environmental variables...")
    load_dotenv()

    nyt_email = os.getenv("NYT_EMAIL")
    nyt_password = os.getenv("NYT_PASSWORD")
    nyt_code = os.getenv("NYT_CODE")
    logger.debug("Successfully loaded environmental variables")

    logger.debug("Adding headless options for selenium...")
    options = Options()
    options.add_argument("window-size=1243x783")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument("--no-sandbox")  # Needed for some environments
    options.add_argument("--disable-dev-shm-usage")  # Helps in Docker

    driver = webdriver.Chrome(options=options)
    logger.debug("Successfully added headless options for selenium")

    redeem_code(driver, nyt_code)

    time.sleep(5)

    redeem_login(driver, nyt_email, nyt_password)

    time.sleep(5)

    finish_redeem(driver)
    
    time.sleep(5)
    
    logger.debug("Successfully ran auto_subscribe_nyt() function!!!")
    driver.quit()