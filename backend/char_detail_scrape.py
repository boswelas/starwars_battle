import asyncio
import time
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def get_char_details(name):
    def replace_spaces(name):
        return name.replace(" ", "_")
    
    formatted_name = replace_spaces(name)
    url = "https://starwars.fandom.com/wiki/{}".format(formatted_name)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_selector('aside.portable-infobox')  # Wait for an element to appear
        content = await page.content()
        await browser.close()
        print(content)

    soup = BeautifulSoup(content, "html.parser")
    details = soup.find("aside", class_="portable-infobox").find_all("section", class_="pi-item")
    return details

# async def main():
#     result = await get_char_details("Luke Skywalker")
#     return result

# if __name__ == "__main__":
#     asyncio.run(main())
