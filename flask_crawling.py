from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

url="https://topis.seoul.go.kr/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.implicitly_wait(0.5)


time.sleep(1)
button = driver.find_element(By.CLASS_NAME,"int-search")
ActionChains(driver).click(button).perform()
time.sleep(1)
id_input =driver.find_element(By.ID,"searchTxt")
ActionChains(driver).send_keys_to_element(id_input,"화곡").perform()
time.sleep(1)
button = driver.find_element(By.CLASS_NAME,"int-btn")
ActionChains(driver).click(button).perform()
time.sleep(1)