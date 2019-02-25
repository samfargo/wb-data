import requests
import csv

api_key = '4bd145ac7e5b3fb30261c010ba3f938e'

r = requests.get('https://api.darksky.net/forecast/4bd145ac7e5b3fb30261c010ba3f938e/37.8267,-122.4233').json()

c = csv.writer(open("weatherdata.csv","w"), lineterminator= '\n')

print(r['timezone'])
print(r['daily']['data'][0]['temperatureHigh'])
print(r['daily']['data'][0]['temperatureLow'])
print(r['daily']['data'][0]['windGust'])
print(r['daily']['data'][0]['precipProbability'])
