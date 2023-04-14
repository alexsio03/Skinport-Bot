# bot.py
import os
import re

import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from discord.ext import commands, tasks

URL = "https://skinport.com/market?sort=percent&order=desc&pricegt=4564&pricelt=91278"
driver = webdriver.Chrome('./chromedriver')

min = 20
oldmin = min
def get_skins():
    driver.get(URL)
    time.sleep(5)
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    skinsfound = []
    results = soup.find(id="content")
    items = results.find_all("div", class_="CatalogPage-item CatalogPage-item--grid")
    for item in items:
        card = item.find("div", class_="ItemPreview-content")
        discount = card.find("div", class_="GradientLabel ItemPreview-discount")
        if(discount):
            num = discount.find("span").text
            num = int(re.findall(r'\d+', discount.find("span").text)[0])
            if(num >= min):
                info = card.find("div", class_="ItemPreview-itemInfo")
                price = info.find("div", class_="Tooltip-link").text
                link = item.find("a", class_="ItemPreview-link", href=True)
                name = item.find("div", class_="ItemPreview-itemTitle").text + " " + item.find("div", class_="ItemPreview-itemName").text
                find = price + " ---> %" + str(num) + " discount (" + name + ")\nhttps://skinport.com" + link['href']
                skinsfound.append(find)
    return skinsfound

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='//',intents=discord.Intents.all())

skindict = {}
@tasks.loop(seconds=7)
async def task_loop():
    global oldmin
    if oldmin != min:
        await bot.get_channel(1095751866765283418).send("Minimum set to: " + str(min) + "%\nSearching...")
        oldmin = min
    skins = get_skins()
    for i in skins:
        ind = hash(i)
        if ind not in skindict:
            await bot.get_channel(1095751866765283418).send("New Item Found!")
            await bot.get_channel(1095751866765283418).send(i)
            skindict[ind] = i
            #<@&915082507685343274>

    
# @bot.command(name='Search')
# async def search(ctx):
#     await ctx.send("Searching...")
#     skins = get_skins(20)
#     joined = '\n\n'.join([str(elem) for elem in skins])

#     await ctx.send(joined)

@bot.command(name="Start")
async def start(ctx):
    await ctx.send("Beginning searching at " + str(min) + "%   (Use **//Min [percentage]** to change minimum percentage)")
    task_loop.start()

@bot.command(name="Min")
async def test(ctx, newmin):
    global min
    min = int(newmin)
    # skins = get_skins(int(min))
    # joined = '\n\n'.join([str(elem) for elem in skins])

    # await ctx.send(joined)

bot.run(TOKEN)
