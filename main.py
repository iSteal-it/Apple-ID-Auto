from selenium import webdriver

capabilities = {
    "browserName": "chrome",
    "version": "81.0",
    "enableVNC": True,
    "enableVideo": True
}

driver = webdriver.Remote(
    command_executor="http://myserverip:4444/wd/hub",
    desired_capabilities=capabilities)

driver.get('www.stackoverflow.com')
print('done')
