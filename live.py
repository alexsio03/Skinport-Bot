# bot.py
# import os
import re
import html

# import discord
# from bs4 import BeautifulSoup
# from discord.ext import commands
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from discord.ext import commands, tasks
import time

CART = "https://skinport.com/cart"
URL = "https://skinport.com/market?sort=date&order=desc"
options = Options()
options.add_argument("user-data-dir=C:\\Users\\Alex Warda\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(URL)
time.sleep(1)
driver.refresh()
driver.set_window_size(1400,1000)
time.sleep(2)
live = driver.find_element(By.CLASS_NAME, "LiveBtn")
live.click()
driver.set_window_size(1000,1000)
time.sleep(1)

skindict = {}
def get_skins():
    items = driver.find_elements(By.CLASS_NAME, "ItemPreview-content")
    for i in range(0, 5):
        # parent = item.find_element(By.CLASS_NAME, "ItemPreview-priceValue")
        # price = parent.find_element(By.CLASS_NAME, "Tooltip-link")
        disc = items[i].find_element(By.CLASS_NAME, "ItemPreview-priceValue");
        #title = items[i].find_element(By.CLASS_NAME, "ItemPreview-itemTitle")
        #name = items[i].find_element(By.CLASS_NAME, "ItemPreview-itemName")
        if(disc):
            if "%" in disc.text:
                price = disc.text[disc.text.index("$") + 1:disc.text.index("\n")]
                discount = disc.text[disc.text.index("−") + 2:disc.text.index("%")]
                if (int(discount) >= 15) and (float(price) >= 2.5):
                    ind = hash(disc)
                    if ind not in skindict:
                        items[i].find_element(By.CLASS_NAME, "ItemPreview-mainAction").click()
                        #print(title.text + " " + name.text)
                        #print("Price: $" + price + "\nDiscount: " + discount + "%\n")
                        skindict[ind] = disc
                        return True

driver.get(CART)
time.sleep(1)
driver.find_element(By.NAME, "tradelock").click()
driver.find_element(By.NAME, "cancellation").click()
driver.find_element(By.XPATH, "//button[@class='SubmitButton CartSummary-checkoutBtn SubmitButton--isFull']").click()
time.sleep(3)

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Iframe for secured card number']"));
driver.find_element(By.XPATH, "/html/body/div/input").send_keys("4899010006746775")
driver.switch_to.default_content()
time.sleep(.5)

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Iframe for secured card expiry date']"));
driver.find_element(By.XPATH, "/html/body/div/input").send_keys("0325")
driver.switch_to.default_content()
time.sleep(.5)

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='Iframe for secured card security code']"));
driver.find_element(By.XPATH, "/html/body/div/input").send_keys("318")
driver.switch_to.default_content()
time.sleep(.5)

driver.find_element(By.XPATH, "//button[@class='adyen-checkout__button adyen-checkout__button--pay']").click()
time.sleep(5)

# while(True):
#     skin = get_skins()
#     if(skin):
#         driver.get(CART)
#         time.sleep(1)
#         driver.find_element(By.NAME, "tradelock").click()
#         driver.find_element(By.NAME, "cancellation").click()
#         driver.find_element(By.XPATH, "//button[@class='SubmitButton CartSummary-checkoutBtn SubmitButton--isFull']").click()
#         time.sleep(1)
#         driver.find_element(By.XPATH, "//input[@autocomplete='cc-number']").send_keys("4899************")
#         driver.find_element(By.XPATH, "//input[@autocomplete='cc-exp']").send_keys("****")
#         driver.find_element(By.XPATH, "//input[@autocomplete='cc-csc']").send_keys("***")
#         driver.find_element(By.XPATH, "//button[@class='adyen-checkout__button adyen-checkout__button--pay']").click()
        
