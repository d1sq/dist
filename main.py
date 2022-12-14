import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--headless")

expected = ''

driver = webdriver.Chrome()
parent_han = driver.window_handles
driver.get('http://dist.kgsu.ru/login/index.php')
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys('101910165')
password.send_keys('9w1jcz')
driver.find_element(By.XPATH, '/html/body/div/div[3]/table/tbody/tr[2]/td[1]/form[1]/p/input[1]').click()
while(True):
    print('cycle never ends')
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
    for idx, sel in enumerate(selectElements, start=1):

        a = Select(sel)
        a.select_by_index(idx)
    driver.find_element(By.NAME, 'finishattempt').click()
    alert = driver.switch_to.alert
    alert.accept()
    print(driver.find_element(By.XPATH, '/html/body/div/div/table/tbody/tr[4]/td[2]').text)
    # driver.quit()
    time.sleep(2)
    driver.get('http://dist.kgsu.ru/mod/quiz/view.php?id=65706')

