from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException ,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import random
import string
import time


DOB = 
delay = 10
QUES = []
ANS = []

chromedriver: str = ""
service = Service(chromedriver)
options = webdriver.ChromeOptions()

while True:
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://iforgot.apple.com")
    enter_mail = driver.find_element(by=By.XPATH,
                                     value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/global-v2/div/idms-flow/div/forgot-password/div/div/div[1]/idms-step/div/div/div/div[2]/div/div[1]/div/div/idms-textbox/idms-error-wrapper/div/div/input")
    response = requests.get("https://pixelpaste.net/pwd")
    data = response.json()
    apple_id = data["apple"]
    enter_mail.send_keys(apple_id)
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/global-v2/div/idms-flow/div/forgot-password/div/div/div[1]/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button").click()
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'subtitle')))
        msg = driver.find_element(by=By.CLASS_NAME, value="subtitle").get_attribute("innerHTML")
    except (NoSuchElementException , TimeoutException) as error:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'app-title')))
        msg = driver.find_element(by=By.CLASS_NAME, value="app-title").get_attribute("innerHTML")

    if msg == "Select which information you would like to reset:":
        print("Apple ID Not Locked")
        driver.close()
        time.sleep(60)
    elif msg == "Select how you want to unlock your account:":
        print("Apple ID Locked")
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/sa/idms-flow/div/section/iforgot-nav/div/div/div[1]/div/div/button[2]").click()
        time.sleep(3)
        driver.close()
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://mail.hostinger.com")
        response = requests.get("https://pixelpaste.net/pwd")
        data = response.json()
        apple_id = data["apple"]
        driver.find_element(by=By.ID,value="rcmloginuser").send_keys(apple_id)
        driver.find_element(by=By.ID, value="rcmloginpwd").send_keys("Krevory123@")
        driver.find_element(by=By.ID, value="rcmloginsubmit").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'message')))
        time.sleep(5)
        driver.find_element(by=By.CLASS_NAME,value="message").click()
        driver.find_element(by=By.CLASS_NAME, value="message").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p a')))
        iforgot_url = driver.find_element(by=By.CSS_SELECTOR,value="p a")
        unlock_url = iforgot_url.get_attribute("href")
        driver.close()
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(unlock_url)
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot/div/iforgot-body/sa/idms-flow/div/section/div/web-reset-options/div[2]/div[2]/div/button").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/iforgot/div/iforgot-body/sa/idms-flow/div/section/div/web-current-password/div[2]/div[1]/idms-textbox/idms-error-wrapper/div/div/input')))
        response = requests.get("https://pixelpaste.net/pwd")
        data = response.json()
        password = data["pass"]
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot/div/iforgot-body/sa/idms-flow/div/section/div/web-current-password/div[2]/div[1]/idms-textbox/idms-error-wrapper/div/div/input").send_keys(password)
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot/div/iforgot-body/sa/idms-flow/div/section/iforgot-nav/div/div/div[1]/div/div/button[2]").click()
        time.sleep(3)
        print("Apple ID Unlocked")
        driver.close()

    elif msg == "Confirm your phone number":
        print("Apple ID Has 2FA")
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/trusted-phone-number/div/div/div[1]/idms-step/div/div/div/div[2]/div/div/div/button')))
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/trusted-phone-number/div/div/div[1]/idms-step/div/div/div/div[2]/div/div/div/button").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"//*/text()[normalize-space(.)='Turn Off']/parent::*")))
        driver.find_element(by=By.XPATH,value="//*/text()[normalize-space(.)='Turn Off']/parent::*").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/verify-birthday/div/div/div[1]/idms-step/div/div/div/div[2]/div/form-fragment-birthday/masked-date/div/idms-error-wrapper/div/div/input')))
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/verify-birthday/div/div/div[1]/idms-step/div/div/div/div[2]/div/form-fragment-birthday/masked-date/div/idms-error-wrapper/div/div/input").send_keys(DOB)
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/verify-birthday/div/div/div[1]/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button[1]").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/verify-security-questions/div/div/div/step-challenge-security-questions/idms-step/div/div/div/div[2]/div/div[1]/div/label")))
        q1 = driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/verify-security-questions/div/div/div/step-challenge-security-questions/idms-step/div/div/div/div[2]/div/div[1]/div/label").get_attribute("innerHTML")
        q2 = driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/verify-security-questions/div/div/div/step-challenge-security-questions/idms-step/div/div/div/div[2]/div/div[2]/div/label").get_attribute("innerHTML")
        for q in  range(len(QUES)):
            if q1 == QUES[q]:
                driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/verify-security-questions/div/div/div/step-challenge-security-questions/idms-step/div/div/div/div[2]/div/div[1]/div/div/idms-textbox/idms-error-wrapper/div/div/input").send_keys(ANS[q])
            if q2 == QUES[q]:
                driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/verify-security-questions/div/div/div/step-challenge-security-questions/idms-step/div/div/div/div[2]/div/div[2]/div/div/idms-textbox/idms-error-wrapper/div/div/input").send_keys(ANS[q])
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/verify-security-questions/div/div/div/step-challenge-security-questions/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button[1]").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/recovery-unenroll-prompt/div/div/div/div/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button[1]")))
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/recovery-unenroll-prompt/div/div/div/div/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button[1]").click()
        pwEnd = ""
        for i in range(4):
            letter = random.choice(string.ascii_lowercase)
            pwEnd = pwEnd + letter
        pw = "https://pixelpaste.net/A2/" + pwEnd
        pseudoPost = requests.get(f"")
        time.sleep(5)
        WebDriverWait(driver , delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/reset-password/div/div/div/div[1]/idms-password/idms-step/div/div/div/div[2]/div/div[1]/div/div[1]/div/new-password/div/idms-textbox/idms-error-wrapper/div/div/input")))
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/reset-password/div/div/div/div[1]/idms-password/idms-step/div/div/div/div[2]/div/div[1]/div/div[1]/div/new-password/div/idms-textbox/idms-error-wrapper/div/div/input").send_keys(pw)
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/reset-password/div/div/div/div[1]/idms-password/idms-step/div/div/div/div[2]/div/div[1]/div/div[2]/div/confirm-password-input/div/idms-textbox/idms-error-wrapper/div/div/input").send_keys(pw)
        driver.find_element(by=By.XPATH,value="/html/body/div[1]/iforgot-v2/app-container/div/iforgot-body/hsa-two-v2/recovery-web-app/idms-flow/div/div/reset-password/div/div/div/div[1]/idms-password/idms-step/div/div/div/div[3]/idms-toolbar/div/div/div/button[1]").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*/text()[normalize-space(.)='Turn Off']/parent::*")))
        driver.find_element(by=By.XPATH,value="//*/text()[normalize-space(.)='Turn Off']/parent::*").click()
        time.sleep(3)
        print("2FA Removed")
        driver.close()
