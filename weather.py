from dotenv import load_dotenv #env for env file
from pprint import pprint #pretty print
import requests
import os

load_dotenv()


def get_current_weather(city="Kansas City"):
#making a API call  |&units=imperial| Temperature by default without adding anything will be in kelvin.
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}'
#.json() because json data is wanted
    weather_data = requests.get(request_url).json()
  #  print(weather_data)

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")
    # Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Shenzhen"
    #run from this file to call all info about a city from API
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)

