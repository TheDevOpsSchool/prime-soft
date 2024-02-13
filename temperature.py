import requests
from datetime import datetime

def get_temperature(api_key, city, date):
    unix_timestamp = int(datetime.strptime(date, "%Y-%m-%d").timestamp())
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    temperature = None

    for item in data['list']:
        if item['dt'] == unix_timestamp:
            temperature = item['main']['temp']
            break

    return temperature

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    temperature = get_temperature(api_key, city, date)
    
    if temperature is not None:
        print(f"The forecasted temperature for {date} in {city} is {temperature}°C")
    else:
        print("Failed to fetch temperature data. Please check the city name, date, and your API key.")

if __name__ == "__main__":
    main()

