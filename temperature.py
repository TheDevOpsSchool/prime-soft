import requests

def get_temperature(api_key, city, country_code, date):
        base_url = "http://api.openweathermap.org/data/2.5/forecast"
            params = {
                            "q": f"{city},{country_code}",
                                    "appid": api_key,
                                            "units": "metric"
                                                }
                response = requests.get(base_url, params=params)
                    data = response.json()

                        # Parse the data to find temperature on the given date
                            for forecast in data['list']:
                                        forecast_date = forecast['dt_txt'].split()[0]
                                                if forecast_date == date:
                                                                temperature = forecast['main']['temp']
                                                                            return temperature
                                                                            return None

                                                                        def main():
                                                                                api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
                                                                                    city = "London"  # Set the default city
                                                                                        country_code = "GB"  # Set the default country code
                                                                                            date = "2024-02-13"  # Set the default date
                                                                                                temperature = get_temperature(api_key, city, country_code, date)
                                                                                                    if temperature is not None:
                                                                                                                print(f"The temperature in {city}, {country_code} on {date} is {temperature}°C.")
                                                                                                                    else:
                                                                                                                                print("Temperature data not available for the given date.")

                                                                                                                                if __name__ == "__main__":
                                                                                                                                        main()

