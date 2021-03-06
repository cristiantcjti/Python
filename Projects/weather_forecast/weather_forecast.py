# TO DO:
# 1. Have display_weather print the weather report.
# 2. Handle network errors by printing a friendly message.
#
# To test your code, open a terminal below and run:
#   python3 weather.py

import requests

API_ROOT = 'https://www.metaweather.com'
API_LOCATION = '/api/location/search/?query='
API_WEATHER = '/api/location/'  # + woeid

def fetch_location(query):
    return requests.get(API_ROOT + API_LOCATION + query).json()

def fetch_weather(woeid):
    return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()

def display_weather(weather):
    print(f"Weather for {weather['title']}:")
    consolidated_weather = weather['consolidated_weather']
    for forecast in consolidated_weather:
        day = forecast['applicable_date']
        min = round(forecast['min_temp'])
        max = round(forecast['max_temp'])
        humid = forecast['humidity']
        print(f'The forecast for {day} is minimum temperature of {min}°C\n'
        f'maximum temperature of {max}°C with {humid} of humidity!')
        print("--------------------------------------------------------------")

def disambiguate_locations(locations):
    print("Ambiguous location! Did you mean:")
    for loc in locations:
        print(f"\t* {loc['title']}")

def weather_dialog():
    try:
        lret = True
        where = ''
        while not where:
            print("Would you like to know the forecast to a place? [Y]=Yes;[N]=No: ")
            answer = input()
            if (answer == 'Y' or answer == 'y'):           
                where = input("What is the place you would like to know the forecast? ")
                locations = fetch_location(where)
                if len(locations) == 0:
                    print("I don't know where that is.")
                elif len(locations) > 1:
                    disambiguate_locations(locations)
                else:
                    woeid = locations[0]['woeid']
                    display_weather(fetch_weather(woeid))
            elif (answer == 'N' or answer == 'n'):
                print("Ok, bye bye!")
                lret = False
                break
            else:
                print("Sorry I do not understand your answer.")
        return lret     
    except requests.exceptions.ConnectionError:
        print("Couldn't connect to server! Is the network up?")


if __name__ == '__main__':
    condition = True
    while condition:
        if (weather_dialog()):
            condition = True
        else:
            condition = False

