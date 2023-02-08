#https://sites.google.com/chromium.org/driver/

#import driver
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyperclip

path = './textFolder'

#sentence corrections
def read_text_file(file_path,  new_file_path ):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines() #read file by list
        print(f'start {new_file_path}')
        w = open(new_file_path, 'w')
        driver.get('https://www.deepl.com/translator#ko/en/')
        driver.implicitly_wait(3)
        for line in lines:
            w.write(line)
            w.write('\n')
            print(line)
            container = driver.find_element(By.CSS_SELECTOR, "#panelTranslateText > div.lmt__sides_container.lmt__sides_container--focus_source > div.lmt__sides_wrapper > section.lmt__side_container.lmt__side_container--source > div.lmt__textarea_container.focus.lmt__textarea_container--focus > div.lmt__inner_textarea_container > d-textarea > div")
            container.send_keys(line)
            driver.implicitly_wait(7)
            driver.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[6]/div/div/div[2]/span[2]/span/span/button').click()

            print(pyperclip.paste())
            w.write(pyperclip.paste())
            driver.implicitly_wait(5)
            driver.find_element(By.CSS_SELECTOR, "#translator-source-clear-button").click()

            w.write('\n\n')
        w.close()
        driver.close()
        print(f'finish! for {new_file_path}')

for file in os.listdir(path):
    driver = webdriver.Chrome('./chromedriver_mac_arm64/chromedriver')
    driver.implicitly_wait(3)

    if file.endswith('.txt'):
        file_path = os.path.join(path, file)
        new_file_path = os.path.join(path,f"translated_dl_{file}")
        read_text_file(file_path,  new_file_path )

