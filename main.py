import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

import config

options = Options()
options.headless = True

counter = 0
def getRandom():
    int = random.choice(ans)
    ans.remove(int)
    return int



expected = ''

driver = webdriver.Chrome(options=options)
parent_han = driver.window_handles
driver.get('http://dist.kgsu.ru/login/index.php')
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys(config.username)
password.send_keys(config.password)
driver.find_element(By.XPATH, '/html/body/div/div[3]/table/tbody/tr[2]/td[1]/form[1]/p/input[1]').click()
while True:
    ans = ['433870276', '2198045', '189605614', '409386288', '586966004', '877055988']
    print('attempt № ' , counter)
    driver.get('http://dist.kgsu.ru/mod/quiz/view.php?id=65706')
    driver.find_element(By.XPATH, '/html/body/div/div[3]/table/tbody/tr/td/div/input').click()
    time.sleep(2)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass
    driver.get('http://dist.kgsu.ru/mod/quiz/attempt.php?id=65706')

    selectElements = driver.find_elements(By.CLASS_NAME, "select")
    for sel in selectElements:
        a = Select(sel)
        a.select_by_value(ans.pop(0))

    driver.find_element(By.NAME, 'finishattempt').click()
    alert = driver.switch_to.alert
    alert.accept()
    print(driver.find_element(By.XPATH, '/html/body/div/div/table/tbody/tr[4]/td[2]').text)
    # driver.quit()
    time.sleep(1)
    counter +=1
    driver.get('http://dist.kgsu.ru/mod/quiz/view.php?id=65706')


