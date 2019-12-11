import requests
import datetime
import hashlib
import json
import requests



def getWeather(city):
    # Make a GET request and read the weather data
    result = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=461ea8b4bdfd7b6a03474176a4a77bbd")
    print(result.content)
    # Using .json() on the result to get a nice easy to use object
    # .content just gives us the string value which we can't access like below
