

from flask import Flask, render_template, request
import requests
from geopy.geocoders import Nominatim

app = Flask(__name__, template_folder='./templates')

# Function to get current weather based on location
def get_weather(location):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(location)
    if location:
        lat = location.latitude
        lon = location.longitude
    else:
        return None, "Location not found"

    api_key = '21b65cff8ba23a5aedf049d3473eb793'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return temperature, description
    except Exception as e:
        return None, str(e)


# Function to suggest outfit based on temperature and preferred style
def suggest_outfit(temperature, preferred_style):
    if temperature > 25:
        if preferred_style == 'casual':
            return "It's hot today! Wear light clothes like shorts and a t-shirt."
        elif preferred_style == 'formal':
            return "It's hot today! Consider light professional attire."
        else:
            return "It's hot today! Choose appropriate attire for the weather."
    elif temperature > 15:
        if preferred_style == 'casual':
            return "It's mild today. A light jacket and jeans should be comfortable."
        elif preferred_style == 'formal':
            return "It's mild today. Opt for a light professional outfit."
        else:
            return "It's mild today. Choose your outfit based on the weather."
    else:
        if preferred_style == 'casual':
            return "It's cold today. Bundle up with a warm jacket, scarf, and gloves."
        elif preferred_style == 'formal':
            return "It's cold today. Ensure your outfit is warm and professional."
        else:
            return "It's cold today. Dress warmly according to the weather."


# Function to suggest clothing for purchase based on temperature
def suggest_clothing_for_purchase(temperature):
    if temperature > 25:
        return "Check out our summer collection: shorts, t-shirts, and sunglasses!"
    elif temperature > 15:
        return "Explore our spring jackets and stylish jeans for today's weather."
    else:
        return "Winter is here! Browse our cozy jackets, scarves, and gloves."


# Route for home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        location = request.form['location']
        temperature, description = get_weather(location)
        if temperature is not None:
            outfit_suggestion = suggest_outfit(temperature, request.form['style'])
            purchase_suggestion = suggest_clothing_for_purchase(temperature)
            weather_data = {
                'temperature': temperature,
                'description': description
            }
            return render_template('index.html', location=location, weather_data=weather_data,
                                   outfit_suggestion=outfit_suggestion, purchase_suggestion=purchase_suggestion)
        else:
            return f"Error fetching weather data: {description}"
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

