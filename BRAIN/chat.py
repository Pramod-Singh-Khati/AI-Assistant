from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import re
import os
import pathlib

ScriptDir = pathlib.Path().absolute()
warnings.simplefilter("ignore")
url = "https://pi.ai/talk"
os.environ['PATH'] += r"c:\SeleniumDrivers"
chrome_options = Options()
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
chrome_options.add_argument("--headless=new")  # Runs
chrome_options.add_argument('--log-level=3')
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(url)

# Wait for 6 seconds
sleep(1)

def Brain(Queary) :


        Input = Queary
        try:
            driver.find_element(by=By.XPATH,
                                value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").send_keys(
                Input)
        except:
            driver.find_element(by=By.XPATH,
                                value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea").send_keys(
                Input)

        sleep(0.5)
        try:
            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click()
        except:
            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").click()

        sleep(6)
        try:
            XpathValue = f'/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div'
            Text = driver.find_element(by=By.XPATH, value=XpathValue).text
            NewText = re.sub(r'\d+\s*', '', Text)
            print(NewText)
            return(NewText)
        except Exception as e:
            print(e)

