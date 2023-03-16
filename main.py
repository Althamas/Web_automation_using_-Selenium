from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(r"C:\Users\LENOVO\Desktop\WEB_DEV\chromedriver"))

driver.get("https://www.python.org/")
time = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
print(len(time))
event = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget li a')
events = {}

for i in range(len(time)):
    events[i] = {
        "time": time[i].text,
        "name": event[i].text,
    }
print(events)
driver.close()
