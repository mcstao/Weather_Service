import requests
from django.shortcuts import render


def get_weather(request):
    weather_api_key = '100fb404761b0f4cab25d6bef491c7d6'
    city = 'Paris'
    lang = 'ru'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&lang={lang}&units=metric'
    data = requests.get(url).json()

    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'wind_direction': data['wind']['deg']
    }

    return render(request, 'get_weather.html', {"weather": weather_data})
