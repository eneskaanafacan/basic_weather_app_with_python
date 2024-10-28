import requests

API_KEY = "6b8130be4231f4aa6dc8e2bd02f8d084"

def get_weather(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    city_data = requests.get(url).json()
    
    if city_data:
        lat = city_data[0]["lat"]
        lon = city_data[0]["lon"]
        
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_data = requests.get(weather_url).json()
        
        if weather_data["cod"] == 200:
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            weather_desc = weather_data["weather"][0]["description"]
            return temperature, humidity, weather_desc
        else:
            return None
    else:
        return None
