import password
import requests


def choose_city(api_key, city):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(url=url, params=params)
    weather = response.json()

    if response.status_code == 200:
        status = weather['weather'][0]['main']
        temp = weather['main']['temp']
        temp_max = weather['main']['temp_max']
        humidity = weather['main']['humidity']

        return f"Today {city} is {status}  \n temperature:{temp}\n Max temperature: {temp_max}\n humidity: {humidity}"
    else:
        return "Error Please check your input"


def main():
    api_key = password.api
    city = input('Please Choose your City: ')
    weather_info = choose_city(api_key, city)
    print(weather_info)


if __name__ == '__main__':
    main()
