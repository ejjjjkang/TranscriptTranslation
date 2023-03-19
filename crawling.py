#https://sites.google.com/chromium.org/driver/

#import driver
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pyperclip
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd



path = './textFolder'
sub_path = './textFolder/translated'

#sentence corrections
def read_text_file(file_path,  new_file_path ):
    with open(file_path, 'r') as f:
        lines = pd.read_csv(f, header=0, usecols=['Text'])
        list_of_csv = [list(row) for row in lines.values]
        print(list_of_csv)
        #lines = f.read().splitlines() #read file by list in txt file
        print(f'start {new_file_path}')
        w = open(new_file_path, 'w')
        driver.get('https://www.deepl.com/translator#ko/en/')
        driver.implicitly_wait(3)
        for line in list_of_csv:
            w.write(line[0])
            w.write('\n')
            try:
                print(line[0])
                container = driver.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[1]/div[3]/div[2]/d-textarea/div')
                container.send_keys(line[0])
                el = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.XPATH, '//*[@id="panelTranslateText"]/div[1]/div[2]/section[2]/div[3]/div[6]/div/div/div[2]/span[2]/span/span/button'))
                el.click()

                print(pyperclip.paste())
                w.write(pyperclip.paste())
                driver.implicitly_wait(10)
                driver.find_element(By.CSS_SELECTOR, "#translator-source-clear-button").click()
            except:
                pass

            w.write('\n\n')
        w.close()
        driver.close()
        print(f'finish! for {new_file_path}')

for file in os.listdir(path):
    driver = webdriver.Chrome('./chromedriver_mac_arm64/chromedriver')
    driver.implicitly_wait(3)

    if file.endswith('.csv'):
        file_path = os.path.join(path, file)
        new_file_path = os.path.join(sub_path,f"translated_dl_{file}")
        read_text_file(file_path,  new_file_path )

