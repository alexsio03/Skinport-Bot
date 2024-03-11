# Skinport Bot
A web scraper to find items that have either a low price or a large discount on the popular online marketplace skinport.com.
This scraper would both try to reserve the item for you so you could purchase it and gain a profit, as well as send a notification
to your server on Discord using the Discord Bot API about the item.

## Tools Used
This project uses the following libraries and tools:
- Discord Bot API
- Chrome Dev Instances
- BeautifulSoup

## Setup

1. If you would like to run this code, you must get a Discord Bot API key and add it to your .env file.
   This could take some work. More details can be found here: https://discord.com/developers/applications
   Clone the repo to begin
```bash
git clone https://github.com/alexsio03/Skinport-Bot
cd Skinport-Bot
```

2. To run the bot -> discord connection:
```bash
python3 bot.py
```

3. To run the scraper in a chrome instance (this will also require updating the chrome path for your sytem):
```bash
python3 live.py
```
