
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


weather_inLocation('sydney', 'au')
weather_inLocation('san francisco', 'us')

