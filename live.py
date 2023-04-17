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
# from discord.ext import commands, tasks
import time

URL = "https://skinport.com/market?sort=date&order=desc"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)
driver.set_window_size(1400,1000)
time.sleep(3)
page = driver.page_source
live = driver.find_element(By.CLASS_NAME, "LiveBtn")
live.click()
time.sleep(1)
driver.set_window_size(800,1000)
time.sleep(1)

def get_skins():
    items = driver.find_element(By.CLASS_NAME, "ItemPreview-content")
    for item in items:
        # parent = item.find_element(By.CLASS_NAME, "ItemPreview-priceValue")
        # price = parent.find_element(By.CLASS_NAME, "Tooltip-link")
        disc = item.find_element(By.XPATH, "//div[@class='GradientLabel ItemPreview-discount']/span");
        # disc = disc_div.find_element(By.TAG_NAME, "span")
        title = item.find_element(By.CLASS_NAME, "ItemPreview-itemTitle")
        name = item.find_element(By.CLASS_NAME, "ItemPreview-itemName")
        print(title.text + " " + name.text)
        print(disc.text + "\n")
        # if(discount):
        #     num = discount.find("span").text
        #     num = int(re.findall(r'\d+', discount.find("span").text)[0])
        #     if(num >= 5):
        #         print("Found cheap item\n")
        #         info = card.find("div", class_="ItemPreview-itemInfo")
        #         price = info.find("div", class_="Tooltip-link").text
        #         link = item.find("a", class_="ItemPreview-link", href=True)
        #         name = item.find("div", class_="ItemPreview-itemTitle").text + " " + item.find("div", class_="ItemPreview-itemName").text
        #         find = price + " ---> %" + str(num) + " discount (" + name + ")\nhttps://skinport.com" + link['href']
        #         btn_div = card.find("div", class_="ItemPreview-actionBtn")
        #         btn = btn_div.find("button", class_="ItemPreview-mainAction")
        #         print(btn)
        #         cart = driver.find_element(By.XPATH, xpath)
        #         cart.click()
        #         return find

get_skins()

# while(True):
#     skin = get_skins()
#     if(skin):
#         print(skin)
#         break

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
