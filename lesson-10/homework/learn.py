'''import json

data = {"name": "Alice", "age": 30, "city": "New York"}

json_data = json.dumps(data, indent=4)
print(json_data)

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)  '''

''' import json
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "employed": True
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # Write JSON with indentation

with open('data.json', 'r') as file:
    loaded_data=json.load(file)
    print(loaded_data)  '''
import json
from datetime import datetime

now = datetime.now()
data = {
    'name': 'John',
    "age": 40,
    'login_time': now.strftime("%Y-%m-%d %H:%M:%S")
}

print(type(data))
s = json.dumps(data)
print(type(s))
print(s)
