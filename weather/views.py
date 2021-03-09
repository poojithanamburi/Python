from django.shortcuts import render
import requests
# Create your views here.
from .forms import CityForm
from .models import City
def index(request):
    url = 'http://api.weatherapi.com/v1/current.json?key=bbc1ff828da341aea48163029210403&q={}&aqi=yes'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()

    weather_Data = []
    for city in cities:

        r= requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperatue': r['current']['temp_f'],
            'icon': r['current']['condition']['icon'],

        }
        weather_Data.append(city_weather)
        print(weather_Data)
    context = {'weather_Data' : weather_Data , 'form': form}
    return render(request, 'weather/weather.html',context)

