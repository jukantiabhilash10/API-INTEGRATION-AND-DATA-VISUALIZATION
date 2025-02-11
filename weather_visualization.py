import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# OpenWeatherMap API details
API_KEY = "9d993757b777112d1bced25bbd11e02c"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Define the city and parameters
CITY = "India"
PARAMS = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

print("Fetching weather data...")  # Debugging Step 1
response = requests.get(BASE_URL, params=PARAMS)
data = response.json()
print("Data fetched successfully!")  # Debugging Step 2

if response.status_code == 200:
    print("Processing data...")  # Debugging Step 3
    dates = []
    temperatures = []
    humidity = []
    
    for entry in data['list']:
        dates.append(datetime.datetime.fromtimestamp(entry['dt']))
        temperatures.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])
    
    print("Data processed! Creating plots...")  # Debugging Step 4
    
    sns.set(style="whitegrid")

    # Plot temperature trends
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temperatures, label='Temperature (°C)', color='orange', marker='o')
    plt.title(f"Temperature Trend for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    print("Showing Temperature plot...")  # Debugging Step 5
    plt.show(block=True)

    # Plot humidity trends
    plt.figure(figsize=(10, 6))
    plt.plot(dates, humidity, label='Humidity (%)', color='blue', marker='o')
    plt.title(f"Humidity Trend for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    print("Showing Humidity plot...")  # Debugging Step 6
    plt.show(block=True)

    print("Script execution completed!")  # Debugging Step 7

else:
    print(f"Failed to fetch data: {data.get('message', 'Unknown error')}")
