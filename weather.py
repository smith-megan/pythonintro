import requests

def get_weather_desc_temp():
  city="Orlando"
  apiKey="not on github"

  url="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiKey+"&units=imperial"
  request=requests.get(url)
  json=request.json()
  # print(json)

  description=json.get("weather")[0].get("description")
  temp_min=json.get("main").get("temp_min")
  temp_max=json.get("main").get("temp_max")
  return {"description":description,
  "temp_min":temp_min,
  "temp_max":temp_max}

def main():
  weather_dict=get_weather_desc_temp()
  # print results
  print("the maximum temperature is:",weather_dict.get("temp_max"))
  print("the minimum temperature is:",weather_dict.get("temp_min"))
  print("today's weather is:", weather_dict.get("description"))

main()