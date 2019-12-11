import requests
import datetime
import hashlib


def getMarvelCharacter(name):
    ts = datetime.datetime.now()
    publicKey = 'e4c6c6bcff21d621eb1306bdad526d24'
    privateKey = '75d190654be7406e192e6903e731cff583ff558d'
    hash = hashlib.md5('{ts}{privateKey}{publicKey}'.format(ts=ts, privateKey=privateKey, publicKey=publicKey).encode())

    request_url = "https://gateway.marvel.com:443/v1/public/characters" \
                  "?nameStartsWith={name}" \
                  "&apikey={apikey}" \
                  "&ts={ts}" \
                  "&hash={hash}"\
        .format(name=name, apikey=publicKey, ts=ts, hash=hash.hexdigest())
    result = requests.get(request_url)

    print(request_url)
    print(result)
    print(result.json())


if __name__ == '__main__':
    getMarvelCharacter('hulk')