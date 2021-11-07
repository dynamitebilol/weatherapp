import requests
import datetime
from config import weather_token

def get_weather(city, weather_token):

    code_to_smile = {
        "Clear": "Ochiq havo \U00002600",
        "Clouds": "Bulutli \U00002601",
        "Rain": "Yomg'ir \U00002614",
        "Drizzle": "Kuchli yomg'ir \U00002614",
        "Thunderstorm": "Momaqaldiroq \U000026A1",
        "Snow": "Qor \U0001F328",
        "Mist": "Tuman \U0001F32B",
        "Haze": "Chang \U0001F32B"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric"
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Oynadan o'zingiz qarang, sizni tushunmadim!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Shahar: {city}\nOb-havo: {cur_weather}C° {wd}\n"
              f"Namlik: {humidity}%\nBosim: {pressure} мм sim.ust\nShamol tezligi: {wind} m/s\n"
              f"Quyosh chiqishi: {sunrise_timestamp}\nQuyosh botishi: {sunset_timestamp}\nKun uzunligi: {length_of_the_day}\n"
              f"Kuningiz yaxshi o'tsin!"
              )

    except Exception as ex:
        print(ex)
        print('Shahar nomini ingliz tilida kiritng!')

def main():
    city = input('Shaharni kiritng: ')
    get_weather(city, weather_token)

if __name__ == '__main__':
    main()
