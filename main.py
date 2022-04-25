from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# killallahandallmuslim@pixelpaste.net
apple_id = "death2allah@isteal-it.com"
delay = 10

chromedriver: str = "/Users/alyadav/Desktop/chromedriver"
service = Service(chromedriver)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

while True:
    driver.get("https://iforgot.apple.com")
    enter_mail = driver.find_element(by=By.XPATH,
                                     value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/global-v2/div/idms-flow/div/forgot-password/div/div/div[1]/idms-step/div/div/div/div[2]/div/div[1]/div/div/idms-textbox/idms-error-wrapper/div/div/input")
    enter_mail.send_keys(apple_id)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/global-v2/div/idms-flow/div/forgot-password/div/div/div[1]/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button").click()
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'subtitle')))
        msg = driver.find_element(by=By.CLASS_NAME, value="subtitle").get_attribute("innerHTML")
    except NoSuchElementException:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'app-title')))
        msg = driver.find_element(by=By.CLASS_NAME, value="app-title").get_attribute("innerHTML")

    if msg == "Select which information you would like to reset:":
        print("Apple ID Not Locked")
        time.sleep(60)
    elif msg == "Select how you want to unlock your account:":
        print("Apple ID Locked")
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/iforgot-nav/div/div/div[1]/div/div/button[2]").click()
        time.sleep(5)
        driver.get("https://mail.hostinger.com")
        driver.find_element(by=By.ID,value="rcmloginuser").send_keys(apple_id)
        driver.find_element(by=By.ID, value="rcmloginpwd").send_keys("Krevory123@")
        driver.find_element(by=By.ID, value="rcmloginsubmit").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'message')))
        driver.find_element(by=By.CLASS_NAME,value="message").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div p p p p a')))
        iforgot_url = driver.find_element(by=By.CSS_SELECTOR,value="div p p p p a")
        unlock_url = iforgot_url.get_attribute("href")
        driver.get(unlock_url)

        time.sleep(60)

    elif msg == "Confirm your phone number":
        print("Apple ID Has 2FA")
        time.sleep(60)
