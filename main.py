from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

char_data = []
url = "https://starwars-force-collection.fandom.com/wiki/Complete_List_of_Cards"

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    page.click('button#adult')
    content = page.content()
    browser.close()

soup = BeautifulSoup(content, "html.parser")
tbodies = soup.find_all("tbody")

for tbody in tbodies:
    rows = tbody.find_all("tr")
    for row in rows:
        details = row.find_all("td")
        if len(details) > 1:
            name = details[1].text.strip()
            image = details[0].text.strip() if details[0].text.strip() else None
            range_val = details[3].text.strip() if len(details) > 3 else None
            base_atk = details[4].text.strip() if len(details) > 4 else None
            base_def = details[5].text.strip() if len(details) > 5 else None
            max_atk = details[6].text.strip() if len(details) > 6 else None
            max_def = details[7].text.strip() if len(details) > 7 else None
            acc = details[8].text.strip() if len(details) > 8 else None
            eva = details[9].text.strip() if len(details) > 9 else None

            char_data.append({
                'name': name,
                'image': image,
                'range': range_val,
                'base_atk': base_atk,
                'base_def': base_def,
                'max_atk': max_atk,
                'max_def': max_def,
                'acc': acc,
                'eva': eva
            })

for char in char_data:
    print(char)
