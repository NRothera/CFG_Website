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
    return result.json()["weather"][0]["description"]


def getMarvelCharacter(name):
    ts = datetime.datetime.now()
    publicKey = 'e4c6c6bcff21d621eb1306bdad526d24'
    privateKey = '75d190654be7406e192e6903e731cff583ff558d'
    hash = hashlib.md5('{ts}{privateKey}{publicKey}'.format(ts=ts, privateKey=privateKey, publicKey=publicKey).encode())

    request_url = "https://gateway.marvel.com:443/v1/public/characters?nameStartsWith={name}&apikey={apikey}&ts={ts}&hash={hash}"\
        .format(name=name, ts=ts, hash=hash.hexdigest(), apikey=publicKey)
    result = requests.get(request_url)

    # print(request_url)
    # print(result)
    # print(result.content)
    json_data = json.loads(result.content)
    print(json_data['data']['results'][0]['thumbnail'])


if __name__ == '__main__':
    getMarvelCharacter('hulk')
