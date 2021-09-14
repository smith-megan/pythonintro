import requests;
response= requests.get('http://api.open-notify.org/astros.json')
# req = requests.request('GET', 'http://api.open-notify.org/astros.json')
json=response.json()

print('the people currently in space:')
for person in json['people']:
  print(person['name'])