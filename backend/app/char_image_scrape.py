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
    url = f"https://starwars.fandom.com/wiki/{formatted_name}"

    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()

        try:
            await page.goto(url, wait_until='domcontentloaded')
            content = await page.content()
             
            soup = BeautifulSoup(content, "html.parser")
            
            no_article_text = soup.find("div", class_="noarticletext")
            if no_article_text:
                await browser.close()
                return {'details': 'Details unavailable'}
            
            await page.wait_for_selector('aside.portable-infobox')
       
            content = await page.content()
            await browser.close()
           
            soup = BeautifulSoup(content, "html.parser")
        except Exception as e:
            print(f"Error during navigation or waiting for selector: {e}")
            await browser.close()
            return {'details': 'Details unavailable'}

    if content:
        infobox = soup.find("aside", class_="portable-infobox")
        if infobox:
            image_tag = infobox.find("img")
            image_url = image_tag['src'] if image_tag else None
            return {'image_url': image_url}
    return {'image': 'Image unavailable'}
