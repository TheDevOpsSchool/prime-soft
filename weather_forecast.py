import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Get your API key from OpenWeatherMap (https://openweathermap.org/)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"Weather: {weather_desc}")
        print(f"Temperature: {temperature}°C")
    else:
        print("City not found or error fetching data")

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    display_weather(weather_data)
