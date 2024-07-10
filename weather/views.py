import requests
from django.shortcuts import render


def get_weather(request):
    weather_api_key = '100fb404761b0f4cab25d6bef491c7d6'
    city = 'Paris'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}'
    result = requests.get(url)
    print(result.text)
    return render(request, 'get_weather.html')
