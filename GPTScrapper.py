import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver  
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.chrome.options import Options 
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
import time

driver = uc.Chrome(use_subprocess=True)
target  = 'https://chat.openai.com/chat'
driver.get(target)
lines = open('creds.txt', 'r').readlines()
cfClear = lines[0].strip()
nextAuthCsrf = lines[1].strip()
nextAuthSession = lines[2].strip()
cookies = [
    {"name":'cf_clearance', "value" : cfClear},
    {"name": '__Host-next-auth.csrf-token', "value": nextAuthCsrf},
    {'name': "__Secure-next-auth.session-token", 'value': nextAuthSession}
]
for c in cookies:
    driver.add_cookie(c)
btn  = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.relative.btn-neutral.ml-auto')))
btn.click()
btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.relative.btn-neutral.ml-auto')))
btn.click()
btn  = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.relative.btn-primary.ml-auto')))
btn.click()
def gettext(request):
     print("Getting chatgpt response")
     inbx = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-0.w-full.resize-none.border-0.bg-transparent.p-0.pr-7')))
     inbx.send_keys(request + '\n')
     output = None
     if check_exists_by_css('.markdown.prose.w-full.break-words.light'):
            outputs = driver.find_elements( By.CSS_SELECTOR, '.markdown.prose.w-full.break-words.light')
            print(len(outputs))
            print(outputs[-1].text)
            output = outputs[-1]
     else:
            output = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.markdown.prose.w-full.break-words.light')))
     oldtxt = "NONE"
     while oldtxt != output.text:
         oldtxt = output.text
         if oldtxt == "":
            oldtxt = "NONE"
         time.sleep(2)
     return output.text

def check_exists_by_css(css):
    try:
        driver.find_element( By.CSS_SELECTOR, css)
    except NoSuchElementException:
        return False
    return True