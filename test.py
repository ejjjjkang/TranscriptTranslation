from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ser = Service('./chromedriver_mac_arm64/chromedriver')
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)
