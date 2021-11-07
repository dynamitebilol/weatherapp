import requests
import datetime
from config import Bot_token, weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=Bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Salom! Shahar nomini yozing va men sizga ob-havo ma'lumotlarini yuboraman. "
                        "(Shahar nomi ingliz tilida yozilishi kerak)!\n"
                        "\nBu bot\U0001F916 @dynamitebilol tomonidan  yaratildi. "
                        "\nBizning botlar\U0001F916 : @bilol_works")


@dp.message_handler()
async def get_weather(message: types.Message):
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
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric"
        )
        data = r.json()

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

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Shahar: {city}\nOb-havo: {cur_weather}C° {wd}\n"
              f"Namlik: {humidity}%\nBosim: {pressure} mm sim.ust\nShamol: {wind} m/s\n"
              f"Quyosh chiqishi: {sunrise_timestamp}\nQuyosh botishi: {sunset_timestamp}\nKun uzunligi: {length_of_the_day}\n"
              f"***Kuningiz yaxshi o'tsin***\n"
              f"\nBu bot\U0001F916 @dynamitebilol tomonidan  yaratildi."
              f"\nBizning botlar\U0001F916 : @bilol_works"
              )

    except:
        await message.reply("\U00002620 Shahar nomini ingliz tilida kiritng \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)

