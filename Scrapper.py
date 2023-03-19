import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
target = ('https://deepai.org/machine-learning-model/text-generator')
driver.set_window_position(0,-1000)

def gettext(prompt):
    driver.get(target)
    item = driver.find_elements(By.CSS_SELECTOR, '.model-input-text-input')
    item[0].send_keys(prompt)
    b = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#modelSubmitButton')))
    b.click()
    textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#place_holder_picture_model')))
    print(textarea.text)
    return textarea.text
