import requests
from django.shortcuts import render
from .models import city
from django.conf import settings

# Create your views here.
def weather_dashboard(request):
    # Read API key securely
    try:
        with open("weather_api.txt", "r") as file:
            api_key = file.read().strip()  # Read and remove any extra spaces/newlines
    except FileNotFoundError:
        return render(request, "index.html", {"weather_data": {"error": "API key file not found!"}})

    if request.method == 'POST':
        weather_data = weather_api(request, api_key)
        return render(request, "weather/index.html", {"weather_data": weather_data})

    return render(request, "weather/index.html")

def weather_api(formData, api_key):
    city_name = formData.POST.get("city")
    api_key = settings.GOOGLE_API_KEY
    geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city_name},+CA&key={api_key}'
    response = requests.get(geocoding_url).json()
    print(response)

    if response['results']:
        location = response['results'][0]['geometry']['location']
        latitude = location['lat']
        longitude = location['lng']

        url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m'
        weather_response = requests.get(url).json()
        return weather_response
    else:
        return {"error": "City not found"}

