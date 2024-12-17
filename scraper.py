import requests
from bs4 import BeautifulSoup
import csv

def scraperapi_url(target_url):
    return f"http://api.scraperapi.com?api_key={SCRAPERAPI_KEY}&url={target_url}"

def collect_all_headers(specs_divs):
    global all_specs_names
    other_specs_names = []
    for div in specs_divs:
        spec_list = div.find('ul')
        for li in spec_list.find_all('li'):
            spec_name = li.find('span', class_='spec-name').get_text(strip=True)
            other_specs_names.append(spec_name)
    other_specs_names = list(dict.fromkeys(other_specs_names))
    all_specs_names = ['prix'] + other_specs_names + all_specs_names

def get_the_cars_for_each_page(car_soup):
    global headersWritten
    car_links = car_soup.find_all("a", class_="occasion-link-overlay", href=True)
    for link in car_links:
        car_url = "https://www.automobile.tn" + link['href']
        with open('mockData.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Use ScraperAPI for the car details page
            res = requests.get(scraperapi_url(car_url))
            car_specs = BeautifulSoup(res.text, 'html.parser')

            main_specs_div = car_specs.find('div', class_='main-specs')
            divided_specs_divs = car_specs.find_all('div', class_='divided-specs')
            specs_divs = [main_specs_div] + divided_specs_divs
            price_div = car_specs.find('div', class_='price')
            price = price_div.find(string=True, recursive=False).strip()
            checked_specs_divs = car_specs.find_all('div', class_='checked-specs')

            if not headersWritten:
                collect_all_headers(specs_divs)
                writer.writerow(all_specs_names)
                headersWritten = True

            car_dict = {key: "NA" for key in all_specs_names}
            car_dict['prix'] = price

            for div in specs_divs:
                spec_list = div.find('ul')
                for li in spec_list.find_all('li'):
                    spec_name = li.find('span', class_='spec-name').get_text(strip=True)
                    spec_value = li.find('span', class_='spec-value').get_text(strip=True)
                    car_dict[spec_name] = spec_value

            for div in checked_specs_divs:
                checked_specs_list = div.find_all('li')
                for li in checked_specs_list:
                    spec_name = li.find('span', class_='spec-value').get_text(strip=True)
                    car_dict[spec_name] = "true"

            vals = [car_dict[header] for header in all_specs_names]
            writer.writerow(vals)


###################################Main#############################################3333

base_url = "https://www.automobile.tn/fr/occasion"
SCRAPERAPI_KEY = "61e23d66512d630e93c6f62269819970"
lastResponseText = ""
headersWritten = False
page_number = 1

with open("options.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    all_specs_names = [line.strip() for line in lines]

while True:
    print(f"Scraping page {page_number}...")

    # Use ScraperAPI for paginated URLs
    page_url = f"{base_url}/{page_number}"
    response = requests.get(scraperapi_url(page_url))

    car_soup = BeautifulSoup(response.text, 'html.parser')
    car_items = car_soup.find('div', class_='articles')

    if car_items == lastResponseText or response.status_code != 200:
        print(f"No cars found on page {page_number}. Breaking loop.")
        break

    get_the_cars_for_each_page(car_soup)
    lastResponseText = car_items
    page_number += 1
