#US city and county web data API

import json
import requests
import urllib2

url = 'http://api.sba.gov/geodata/all_links_for_city_of/CITY_NAME/STATE_ABBREVIATION.FORMAT'

params = {'CITY_NAME':'trenton', 'STATE_ABBREVIATION':'nj','FORMAT':'json'}

resp = requests.get(url = url, params = params)


#resp = requests.get('http://api.sba.gov/geodata/all_links_for_city_of/trenton/nj.json')
data = resp.json()
print data



