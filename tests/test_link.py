from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

link = driver.find_element(By.TAG_NAME, "a")
link.click()

print("Link clicked successfully")

driver.quit()
