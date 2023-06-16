from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "num1")
x = x_element.text
y_element = browser.find_element(By.ID, "num2")
y = y_element.text
result = str(int(x) + int(y))

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(result)

button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
button1.click()

time.sleep(30)
browser.quit()
