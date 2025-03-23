from bs4 import BeautifulSoup


with open('weather.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

forecast = []
rows = soup.find('tbody').find_all('tr')
for row in rows:
    day = row.find_all('td')[0].text
    temperature = row.find_all('td')[1].text
    condition = row.find_all('td')[2].text
    forecast.append({'day': day, 'temperature': temperature, 'condition': condition})

for entry in forecast:
    print(f"Day: {entry['day']}, Temperature: {entry['temperature']}, Condition: {entry['condition']}")


max_temp = max(forecast, key=lambda x: int(x['temperature'].replace('°C', '')))
print(f"Day with the highest temperature: {max_temp['day']} ({max_temp['temperature']})")


sunny_days = [entry['day'] for entry in forecast if entry['condition'] == 'Sunny']
print(f"Days with 'Sunny' condition: {', '.join(sunny_days)}")

