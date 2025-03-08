import requests
from django.shortcuts import render
from .models import city

# Create your views here.
def weather_dashboard(request):
    # Read API key securely
    try:
        with open("weather_api.txt", "r") as file:
            api_key = file.read().strip()  # Read and remove any extra spaces/newlines
    except FileNotFoundError:
        return render(request, "index.html", {"weather_data": {"error": "API key file not found!"}})

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

def weather_api(formData):
    uid = formData.POST("uid")
    city_name = formData.POST("city")
    # Read API key securely
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m'
    response = requests.post(url).json()

