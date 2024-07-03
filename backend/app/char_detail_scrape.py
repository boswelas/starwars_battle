import asyncio
import os
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
        browser = await pw.chromium.connect_over_cdp(os.environ['BROWSER_PLAYWRIGHT_ENDPOINT'])
        print(f"opened browser")
        context = await browser.new_context()
        print(f"new context")
        page = await context.new_page()
        print(f"opened page")
        # browser = await pw.chromium.launch()
        # print("opened browser")
        # page = await browser.new_page()
        # print("new page")
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
            details = defaultdict(list)
            sections = infobox.find_all("section", class_="pi-item")
            for section in sections:
                section_header = section.find("h2", class_="pi-item")
                label_elements = section.find_all("h3", class_="pi-data-label")
                value_elements = section.find_all("div", class_="pi-data-value")
                
                section_header_text = section_header.get_text(strip=True) if section_header else None
                
                for label, value in zip(label_elements, value_elements):
                    # Remove citations and commas
                    clean_values = [re.sub(r'\[\d+\]', '', v).replace(',', '').strip() for v in value.stripped_strings]
                    
                    processed_values = []
                    buffer = ''
                    inside_parentheses = False

                    for v in clean_values:
                        if '(' in v and ')' not in v:
                            buffer = v
                            inside_parentheses = True
                        elif inside_parentheses:
                            buffer += ' ' + v
                            if ')' in v:
                                if processed_values:
                                    processed_values[-1] += ' ' + buffer.strip()
                                buffer = ''
                                inside_parentheses = False
                        else:
                            if v.startswith('(') and v.endswith(')'):
                                if processed_values:
                                    processed_values[-1] += ' ' + v
                            else:
                                processed_values.append(v.strip())

                    # If there's anything left in the buffer, append it
                    if buffer and processed_values:
                        processed_values[-1] += ' ' + buffer.strip()
                    
                    # Remove empty values
                    processed_values = [value for value in processed_values if value]

                    # Ensure a space before parentheses
                    processed_values = [re.sub(r'\s*\(\s*', ' (', v).replace(' )', ')') for v in processed_values]

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
            return {'details': details_list, 'image_url': image_url}
    return {'details': 'Details unavailable'}
