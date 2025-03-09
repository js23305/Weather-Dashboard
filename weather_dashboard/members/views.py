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
        weather_data = weather_api(request)
        return render(request, "weather/index.html", {"weather_data": weather_data})

    return render(request, "weather/index.html")

def weather_api(formData):
    uid = formData.POST("uid")
    city_name = formData.POST("city")

    geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city_name},+CA&key=AIzaSyCzvqhwadU4iM5BPMYAFzz14_4doR8069c'
    response = requests.POST(geocoding_url).json()
    print(response)


    # Read API key securely
    #url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m'
    #response = requests.post(url).json()

