
# import requests

# url = "https://api.open-meteo.com/v1/forecast?latitude=5.6037&longitude=-0.1870&current=temperature_2m,relative_humidity_2m,wind_speed_10m"   

# response = requests.get(url)
# response.status_code

# print(response.status_code)
# print(response.json())

from pprint import pprint
import requests
r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=5.6037&longitude=-0.1870&current=temperature_2m,relative_humidity_2m,wind_speed_10m")
pprint(r.json())