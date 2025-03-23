import requests
from bs4 import BeautifulSoup
import json

def scrape_laptops():
    base_url = 'https://www.demoblaze.com/'
    laptops = []

    def get_laptops_from_page(soup):
        items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
        for item in items:
            name = item.find('h4', class_='card-title').text.strip()
            price = item.find('h5').text.strip()
            description = item.find('p', class_='card-text').text.strip()
            laptops.append({
                'name': name,
                'price': price,
                'description': description
            })

    page = 1
    while True:
        response = requests.get(f'{base_url}index.html#')
        soup = BeautifulSoup(response.text, 'html.parser')
        get_laptops_from_page(soup)

        next_button = soup.find('button', id='next2')
        if next_button is None or 'disabled' in next_button.get('class', []):
            break
        page += 1

    return laptops

def save_to_json(data, filename='laptops.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    laptops = scrape_laptops()
    save_to_json(laptops)