from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.ID, "treasure")
x_element_value = x_element.get_attribute("valuex")
y = calc(x_element_value)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

checkbox1 = browser.find_element(By.ID, "robotCheckbox")
checkbox1.click()

radiobutton1 = browser.find_element(By.ID, "robotsRule")
radiobutton1.click()

button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button1.click()

time.sleep(30)
browser.quit()
