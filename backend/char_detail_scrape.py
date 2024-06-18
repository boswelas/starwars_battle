import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def get_char_details(name):
    def replace_spaces(name):
        return name.replace(" ", "_")

    formatted_name = replace_spaces(name)
    print("formatted name:", formatted_name)
    url = f"https://starwars.fandom.com/wiki/{formatted_name}"

    async with async_playwright() as pw:
        browser = await pw.chromium.launch()  # Set headless=False for debugging
        print("opened browser")
        page = await browser.new_page()
        print("new page")
        try:
            await page.goto(url, wait_until='domcontentloaded', timeout=120000)  # Increase timeout to 120 seconds
            print("went to:", url)
            await page.wait_for_selector('aside.portable-infobox', timeout=60000)  # Increase timeout to 60 seconds
            print("selector found")
        except Exception as e:
            print(f"Error during navigation or waiting for selector: {e}")
            await browser.close()
            return False
        print("getting content")
        content = await page.content()
        print("got content. closing browser")
        await browser.close()

    if content:
        print("in the soup")
        soup = BeautifulSoup(content, "html.parser")
        infobox = soup.find("aside", class_="portable-infobox")
        if infobox:
            details = []
            sections = infobox.find_all("section", class_="pi-item")
            for section in sections:
                label = section.find("h3", class_="pi-data-label")
                value = section.find("div", class_="pi-data-value")
                if label and value:
                    details.append({
                        'label': label.get_text(strip=True),
                        'value': value.get_text(strip=True)
                    })
            image_tag = infobox.find("img")
            image_url = image_tag['src'] if image_tag else None
            return {'details': details, 'image_url': image_url}
    return False

# Example usage:
# asyncio.run(get_char_details("Admiral Ackbar"))
