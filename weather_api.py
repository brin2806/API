
import urllib2
import json
# obtain personal api from openweather channel
weather_api = '82baddfd8ae36af172ae71dcb0dfce78'


def weather_inLocation(cityname, country):
    # find the url for the webpage
    final_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityname +',' + country + '&APPID='+ weather_api
    #use urllib2 to open the web page and assign it to a variable
    json_object = urllib2.urlopen(final_url)
    # load the data the json object and assign it to a variable
    data = json.load(json_object)
    max_temp_kelvin = data['main']['temp_max']
    max_temp_celsius = int(max_temp_kelvin) - 273.15
    cloud_cover = data['weather'][0]['description']
    print "In {}, {}, the max temperature is {} degrees celsius and cloud cover is {}"\
        .format(cityname, country, max_temp_celsius, cloud_cover )


weather_inLocation('sydney', 'australia')
weather_inLocation('san francisco', 'us')
weather_inLocation('london','uk')



'''This is my attempt of week 4 assignment question 1 '''

#acess api using requests library

import requests




def weather(cityname, country):
    next_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityname +',' + country + '&APPID='+ weather_api

    params = dict(cityname = cityname, country = country)


    resp = requests.get(url = next_url, params = params)
    data = json.loads(resp.text)

    max_temp_kelvin = data['main']['temp_max']
    max_temp_celsius = int(max_temp_kelvin) - 273.15
    cloud_cover = data['weather'][0]['description']
    print "In {}, {}, the max temperature is {} degrees celsius and cloud cover is {}"\
        .format(cityname, country, max_temp_celsius, cloud_cover )

print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
weather('sydney', 'australia') # gives same response as using urlib2
weather('san francisco','us' )
weather('london', 'uk')

'''I could not access the list of cities...got stuck'''

print '====================================================================='
def weather_in_cities(country):
    url_city = 'https://raw.githubusercontent.com/David-Haim/CountriesToCitiesJSON/master/countriesToCities.json'

    resp = requests.get(url_city)
    data = resp.json()

    print data

weather_in_cities('China') # THIS CODE DOES NOT WORK

