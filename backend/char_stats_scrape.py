import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def get_char_data():
    char_data = {}
    url = "https://starwars-force-collection.fandom.com/wiki/Complete_List_of_Cards"

    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        await page.click('button#adult')
        content = await page.content()
        await browser.close()

    soup = BeautifulSoup(content, "html.parser")
    tbodies = soup.find_all("tbody")[:-3]

    for tbody in tbodies:
        rows = tbody.find_all("tr")
        for row in rows:
            details = row.find_all("td")
            if len(details) > 1:
                name = details[1].text.strip()
                image = details[0].find("a")["href"]
                range_val = details[3].text.strip() if len(details) > 3 else None
                base_atk = details[4].text.strip() if len(details) > 4 else None
                base_def = details[5].text.strip() if len(details) > 5 else None
                max_atk = details[6].text.strip() if len(details) > 6 else None
                max_def = details[7].text.strip() if len(details) > 7 else None
                acc = details[8].text.strip() if len(details) > 8 else None
                eva = details[9].text.strip() if len(details) > 9 else None
                
                cleaned_name = re.sub(r'\[.*?\]', '', name).strip()

                # Check that all values are the correct type 
                if (base_atk.isdigit() and
                    base_def.isdigit() and
                    max_atk.isdigit() and
                    max_def.isdigit() and
                    acc.isdigit() and
                    eva.isdigit()):
                    print("ranges are valid for ", cleaned_name)   
                    # Avoid duplicate characters
                    if cleaned_name not in char_data or int(max_atk) > int(char_data[cleaned_name]['max_atk']):
                        print("adding ", cleaned_name)
                        char_data[cleaned_name] = {
                            'name': cleaned_name,
                            'image': image,
                            'range': range_val,
                            'base_atk': base_atk,
                            'base_def': base_def,
                            'max_atk': max_atk,
                            'max_def': max_def,
                            'acc': acc,
                            'eva': eva
                        }

    char_data_filtered = {
        key: value for key, value in char_data.items()
        if all(value.values())
    }

    char_data_filtered_list = list(char_data_filtered.values())
    print("ran file")

    return char_data_filtered_list
