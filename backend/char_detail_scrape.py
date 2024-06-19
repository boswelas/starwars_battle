import asyncio
import re
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from collections import defaultdict

async def get_char_details(name):
    def replace_spaces(name):
        return name.replace(" ", "_")

    formatted_name = replace_spaces(name)
    print("formatted name:", formatted_name)
    url = f"https://starwars.fandom.com/wiki/{formatted_name}"

    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        print("opened browser")
        page = await browser.new_page()
        print("new page")
        try:
            await page.goto(url, wait_until='domcontentloaded')
            print("went to:", url)
            await page.wait_for_selector('aside.portable-infobox')
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
            details = defaultdict(list)
            sections = infobox.find_all("section", class_="pi-item")
            for section in sections:
                section_header = section.find("h2", class_="pi-item")
                label_elements = section.find_all("h3", class_="pi-data-label")
                value_elements = section.find_all("div", class_="pi-data-value")
                
                section_header_text = section_header.get_text(strip=True) if section_header else None
                
                for label, value in zip(label_elements, value_elements):
                    # Remove citations
                    clean_values = [re.sub(r'\[\d+\]', '', v).strip() for v in value.stripped_strings]

                    # Process the values
                    processed_values = []
                    buffer = ''
                    inside_parentheses = False

                    for v in clean_values:
                        # Remove spaces before commas within values
                        v = re.sub(r'\s+,', ',', v)

                        if v == ',':  # Handle standalone comma
                            if processed_values:
                                processed_values[-1] += v
                        elif re.match(r'.*\(.*\).*', v):  # Complete parenthesis in the string
                            if buffer:
                                buffer += ' ' + v
                                processed_values.append(buffer.strip())
                                buffer = ''
                            else:
                                processed_values.append(v.strip())
                        elif re.match(r'\(.*', v):  # Opening parenthesis without closing
                            inside_parentheses = True
                            buffer += ' ' + v if buffer else v
                        elif re.match(r'.*\)', v):  # Closing parenthesis
                            inside_parentheses = False
                            buffer += ' ' + v
                            if processed_values:
                                processed_values[-1] += ' ' + buffer.strip()
                            else:
                                processed_values.append(buffer.strip())
                            buffer = ''
                        elif inside_parentheses:
                            buffer += ' ' + v
                        elif re.match(r'\d', v):  # Numbers
                            if buffer:
                                processed_values.append(buffer.strip())
                            buffer = v
                        else:
                            if buffer:
                                buffer += ' ' + v
                                processed_values.append(buffer.strip())
                                buffer = ''
                            else:
                                processed_values.append(v.strip())

                    if buffer:
                        processed_values.append(buffer.strip())

                    # Remove empty values
                    processed_values = [value for value in processed_values if value]

                    if processed_values:
                        details[section_header_text].append({
                            'label': label.get_text(strip=True),
                            'values': processed_values
                        })

            details_list = [
                {'section_header': key, 'details': value}
                for key, value in details.items()
            ]
            image_tag = infobox.find("img")
            image_url = image_tag['src'] if image_tag else None
            print(details_list)
            return {'details': details_list, 'image_url': image_url}
    return False

# Example usage
asyncio.run(get_char_details("Han Solo"))
