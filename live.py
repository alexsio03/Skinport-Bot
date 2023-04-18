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
driver.refresh()
driver.set_window_size(1400,1000)
time.sleep(3)
live = driver.find_element(By.CLASS_NAME, "LiveBtn")
live.click()
time.sleep(1)
driver.set_window_size(800,1000)
time.sleep(1)

skindict = {}
def get_skins():
    items = driver.find_elements(By.CLASS_NAME, "ItemPreview-content")
    for i in range(0, 5):
        # parent = item.find_element(By.CLASS_NAME, "ItemPreview-priceValue")
        # price = parent.find_element(By.CLASS_NAME, "Tooltip-link")
        disc = items[i].find_element(By.CLASS_NAME, "ItemPreview-priceValue");
        # disc = disc_div.find_element(By.TAG_NAME, "span")
        title = items[i].find_element(By.CLASS_NAME, "ItemPreview-itemTitle")
        name = items[i].find_element(By.CLASS_NAME, "ItemPreview-itemName")
        if(disc):
            if "%" in disc.text:
                price = disc.text[disc.text.index("$") + 1:disc.text.index("\n")]
                discount = disc.text[disc.text.index("−") + 2:disc.text.index("%")]
                if (int(discount) >= 15) and (float(price) >= 3):
                    ind = hash(disc)
                    if ind not in skindict:
                        cart_btn = items[i].find_element(By.CLASS_NAME, "ItemPreview-mainAction")
                        cart_btn.click()
                        print(title.text + " " + name.text)
                        print("Price: $" + price + "\nDiscount: " + discount + "%\n")
                        skindict[ind] = disc
                        return True
        return False

while(True):
    skin = get_skins()
    if(skin):
        driver.get(CART)
        time.sleep(1)
        div = driver.find_element(By.CLASS_NAME, "CartSummary-payment")
        check1 = driver.find_element(By.ID, "cb-tradelock-5")
        check1.click()
        check2 = driver.find_element(By.ID, "cb-cancellation-6")
        check2.click()
        submit = driver.find_element(By.XPATH, "//button[@class='SubmitButton CartSummary-checkoutBtn SubmitButton--isFull']")
        submit.click()
        time.sleep(2)

# load_dotenv()

# TOKEN = os.getenv('DISCORD_TOKEN')

# bot = commands.Bot(command_prefix='//',intents=discord.Intents.all())

# skindict = {}
# @tasks.loop(seconds=7)
# async def task_loop():
#     global oldmin
#     if oldmin != min:
#         await bot.get_channel(1095751866765283418).send("Minimum set to: " + str(min) + "%\nSearching...")
#         oldmin = min
#     skins = get_skins()
#     for i in skins:
#         ind = hash(i)
#         if ind not in skindict:
#             await bot.get_channel(1095751866765283418).send("New Item Found!")
#             await bot.get_channel(1095751866765283418).send(i)
#             skindict[ind] = i
#             #<@&915082507685343274>

    
# # @bot.command(name='Search')
# # async def search(ctx):
# #     await ctx.send("Searching...")
# #     skins = get_skins(20)
# #     joined = '\n\n'.join([str(elem) for elem in skins])

# #     await ctx.send(joined)

# @bot.command(name="Start")
# async def start(ctx):
#     await ctx.send("Beginning searching at " + str(min) + "%   (Use **//Min [percentage]** to change minimum percentage)")
#     task_loop.start()

# @bot.command(name="Stop")
# async def start(ctx):
#     await ctx.send("Terminating search")
#     task_loop.stop()

# @bot.command(name="Min")
# async def test(ctx, newmin):
#     global min
#     min = int(newmin)
#     # skins = get_skins(int(min))
#     # joined = '\n\n'.join([str(elem) for elem in skins])

#     # await ctx.send(joined)

# bot.run(TOKEN)
