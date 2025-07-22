from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    weather_data = get_weather()
    return render_template('index.html', weather=weather_data)

def get_weather():
    api_key = 'affe0b9575fc0978c54a7d91af9483a1'  # Replace with your actual API key
    lat = 45.5017  # Latitude for Montreal
    lon = -73.5673  # Longitude for Montreal
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to connect to OpenWeatherMap API: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)