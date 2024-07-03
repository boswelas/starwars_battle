import asyncio
import os
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from collections import defaultdict

async def scrape_char_image(name):
    def replace_spaces(name):
        return name.replace(" ", "_")

    formatted_name = replace_spaces(name)
    print("formatted name:", formatted_name)
    url = f"https://starwars.fandom.com/wiki/{formatted_name}"

    async with async_playwright() as pw:
        # browser = await pw.chromium.launch()
        # print("opened browser")
        # page = await browser.new_page()
        # print("new page")
        browser = await pw.chromium.connect_over_cdp(os.environ['BROWSER_PLAYWRIGHT_ENDPOINT'])
        print(f"opened browser")
        context = await browser.new_context()
        print(f"new context")
        page = await context.new_page()
        print(f"opened page")
        try:
            await page.goto(url, wait_until='domcontentloaded')
            print("went to:", url)
            content = await page.content()
            print("got content")
             
            soup = BeautifulSoup(content, "html.parser")
            
            no_article_text = soup.find("div", class_="noarticletext")
            if no_article_text:
                print("No article text found. Article does not exist.")
                await browser.close()
                return {'details': 'Details unavailable'}
            print("No noarticletext found, proceeding to find infobox.")
            
            await page.wait_for_selector('aside.portable-infobox')
            print("selector found")
       
            content = await page.content()
            print("got content again")
            await browser.close()
           
            soup = BeautifulSoup(content, "html.parser")
        except Exception as e:
            print(f"Error during navigation or waiting for selector: {e}")
            await browser.close()
            return {'details': 'Details unavailable'}

    if content:
        print("in the soup")
        infobox = soup.find("aside", class_="portable-infobox")
        if infobox:
            image_tag = infobox.find("img")
            image_url = image_tag['src'] if image_tag else None
            print("image url: ", image_url)
            return {'image_url': image_url}
    return {'image': 'Image unavailable'}
