document.getElementById('weather-form'),addEventListener('submit', function(event) {
    event.preventDefault();

    // Get the city name from the input field
    let city = this.document.getElementById('city').ariaValueMax;
    fetchWeather(city);
});

function fetchWeather(city) {
    const apiKey = 'replace_with_your_api_key';
    const url = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    // Fetch the weather data from the OpenWeatherMap API
    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.cod === 200) {
                // Update the weather information
                document.getElementById('city-name').textContent = '${data.name}, ${data.sys.country}';
                document.getElementById('temperature').textContent = 'Temperature: ${data.sys.temp} °C';
                document.getElementById('description').textContent = 'Description: ${data.weather[0].decription}';

                // Change background color based on weather conditions
                updateBackgroundColor(data.weather[0].main);
            } else {
                alert('City not found');
            }
        })
        .catch(error => console.error('Error fetching weather data:', error));
}

function updateBackgroundColor(weather) {
    let body = document.body;

    // Remove any existing background classes
    body.classList.remove('sunny', 'cloudy', 'rainy', 'snowy');

    if (weatherCondition.toLowerCase() === 'clear') {
        body.classList.add('sunny');
    } else if (weatherCondition.toLowerCase() === 'clouds') {
        body.classList.add('cloudy');
    } else if (weatherCondition.toLowerCase() === 'rain') {
        body.classList.add('rainy');
    } else if (weatherCondition.toLowerCase() === 'snow') {
        body.classList.add('snowy');
    }
}
