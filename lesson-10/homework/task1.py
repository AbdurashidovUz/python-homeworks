import requests


url = 'https://api.openweathermap.org/data/2.5/weather?q=Tashkent&appid=095569ceed32310a417b21224e8e1a92&units=metric'

response = requests.get(url)

data = response.json()
print (data)
temperature = data['main']['temp']
humidity = data['main']['humidity']
weather_description = data['weather'][0]['description']

print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Weather Description:", weather_description)
