import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import requests
from geopy.geocoders import Nominatim


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


# Function to fetch weather data and update GUI
def fetch_weather():
    location = simpledialog.askstring("Location", "Enter your city or location:")
    if location:
        temperature, description = get_weather(location)
        if temperature is not None:
            weather_text.set(f"Current temperature in {location}: {temperature}°C\nWeather: {description}")
            outfit_text.set(suggest_outfit(temperature, preferred_style.get()))
            purchase_suggestion_text.set(suggest_clothing_for_purchase(temperature))
        else:
            messagebox.showerror("Error", f"Could not fetch weather data.\nError: {description}")
    else:
        messagebox.showwarning("Warning", "Please enter a location.")


# Initialize Tkinter app
root = tk.Tk()
root.title("Weather App")

# Weather frame
weather_frame = ttk.Frame(root, padding="20")
weather_frame.grid(row=0, column=0, padx=20, pady=20)

# Weather display
weather_text = tk.StringVar()
weather_label = ttk.Label(weather_frame, textvariable=weather_text, wraplength=300)
weather_label.grid(row=0, column=0, padx=10, pady=10)

# Outfit suggestion
outfit_text = tk.StringVar()
outfit_label = ttk.Label(weather_frame, textvariable=outfit_text, wraplength=300)
outfit_label.grid(row=1, column=0, padx=10, pady=10)

# Purchase suggestion
purchase_suggestion_text = tk.StringVar()
purchase_suggestion_label = ttk.Label(weather_frame, textvariable=purchase_suggestion_text, wraplength=300)
purchase_suggestion_label.grid(row=2, column=0, padx=10, pady=10)

# Style selection (dropdown)
style_label = ttk.Label(weather_frame, text="Select preferred style:")
style_label.grid(row=3, column=0, padx=10, pady=10)

preferred_style = tk.StringVar()
style_combobox = ttk.Combobox(weather_frame, textvariable=preferred_style, values=["casual", "formal", "any"])
style_combobox.current(0)
style_combobox.grid(row=3, column=1, padx=10, pady=10)

# Fetch weather button
fetch_button = ttk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.grid(row=1, column=0, padx=20, pady=20)

# Run the Tkinter main loop
root.mainloop()
