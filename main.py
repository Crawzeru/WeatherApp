import requests
import json

# OpenWeatherMap API anahtarınızı buraya ekleyin
API_KEY = 'Your_API_Key'


def get_weather(city):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(base_url)
        data = response.json()

        if data['cod'] == 200:
            weather_data = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            print(f'Hava Durumu: {weather_data.capitalize()}')
            print(f'Sıcaklık: {temperature}°C')
            print(f'Nem: {humidity}%')
            print(f'Rüzgar Hızı: {wind_speed} m/s')
        else:
            print('Şehir bulunamadı.')

    except Exception as e:
        print(f'Hata oluştu: {e}')


if __name__ == "__main__":
    city = input("Hava durumu bilgisini almak istediğiniz şehri girin: ")
    get_weather(city)
