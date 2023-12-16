from django.shortcuts import render
from django.conf import settings
import requests
from .models import City
from .forms import CityForm


def index(request):
    api_key = settings.OPENWEATHER_API_KEY
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    error_message = ""

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data["name"].title()
            if City.objects.filter(name=city_name).count() == 0:
                r = requests.get(url.format(city_name, api_key)).json()
                if r["cod"] == 200:
                    form.save()
                else:
                    error_message = "This city doesn't exist in our database :("
            else:
                error_message = "This city is already in our database"
    else:
        form = CityForm()

    city_names = City.objects.all()
    weather_data = []

    for city_name in city_names:
        city_weather = requests.get(url.format(city_name, api_key)).json()
        weather = {
            "city_name": city_name,
            "temperature": city_weather["main"]["temp"],
            "sensed_temperature": city_weather["main"]["feels_like"],
            "description": city_weather["weather"][0]["description"],
            "icon": city_weather["weather"][0]["icon"],
        }
        weather_data.append(weather)

    return render(request, "index.html", {"weather_data": weather_data, "form": form, "error_message": error_message})
