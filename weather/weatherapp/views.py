from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import requests


def index(request):
    api_key = settings.OPENWEATHER_API_KEY
    city = "Gryfice"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    city_weather = requests.get(url).json()

    weather = {
        "city": city,
        "temperature": city_weather["main"]["temp"],
        "sensed_temperature": city_weather["main"]["feels_like"],
        "description": city_weather["weather"][0]["description"],
        "icon": city_weather["weather"][0]["icon"],
    }

    return render(request, "index.html", {"weather": weather})
