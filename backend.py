import requests
import os

API_KEY = os.getenv("weather_api_key")


def get_data(place, forcast_days):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
        response = requests.get(url=url)
        data = response.json()
        filtered_data = data["list"]
        nr_values = 8 * forcast_days
        filtered_data = filtered_data[:nr_values]
        return filtered_data
    except KeyError:
        print(f"City {place} not found")



if __name__ == "__main__":
    print(get_data(place="Toronto", forcast_days=5))
