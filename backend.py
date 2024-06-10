import requests

API_KEY = "7147511e0613505f05495615ba5fe57c"


def get_data(place, forcast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [d["main"]["temp"] for d in filtered_data]
    elif kind == "Sky":
        filtered_data = [d["weather"][0]["main"] for d in filtered_data]
    return data


if __name__ == "__main__":
    print(get_data(place="Toronto", forcast_days=3, kind="Temperature"))
