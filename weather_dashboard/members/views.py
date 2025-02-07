import requests
from django.shortcuts import render
from .models import city

# Create your views here.
def weather_dashboard(request):
    f = open("weather_api.txt", "r")    
    weather_data = None

    if request.method == 'POST':
        city_name = request.Post.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}"
        response = requests.get(url).json()

        if response["cod"] == 200:
            weather_data = {
                "city": response["name"],
                "temperature": response["main"]["temp"],
                "humidity": response["main"]["humidity"],
                "description": response["weather"][0]["description"],
                "icon": response["weather"][0]["icon"]
            }

        else:
            weather_data = {"error": "City not found!"}

    return render(request, "weather/index.html", {"weather_data": weather_data})    