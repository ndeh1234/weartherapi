import requests  # Import the request module
import os

from datetime import datetime  # Imports the datetime module


# Main method
def main():
    key = os.environ.get('WEATHER_KEY')

    # printing a welcome message
    print('Welcome to your five day forecast!')

    # Taking input from users
    city = input('Enter the name of the city you want the weather forecast for: ')
    country = input('Enter the 2 character country abbreviation. ')

    # setting parameters
    parameters = {'q': '', 'units': 'imperial', 'appid': key}
    parameters['q'] = city.lower() + ',' + country.lower()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&' \
          'APPID = '.format(city)

    # make a request
    query = {'q': {}, 'units': 'imperial', 'appid': key}
    forecast = requests.get(url, params=query).json()

    temp = forecast['main']['temp']
    wind_speed = forecast['wind']['speed']
    description = forecast['weather'][0]['description']


    print(f'The weather is {description},the wind speed is {wind_speed}, and the temperature is {temp:.2f}F.')




if __name__ == '__main__':
    main()