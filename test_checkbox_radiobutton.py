from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

checkbox1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
checkbox1.click()

radiobutton1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
radiobutton1.click()

button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button1.click()

time.sleep(30)
browser.quit()
