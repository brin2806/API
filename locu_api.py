import urllib2 # has function in it that allows us to open up a url
import json

# create a variable to house api key"
locu_api = "1ac07cd2c3cf46815d50a43e0707d409daa94505"

# get query url link
# assign the url to a variable
url = 'https://api.locu.com/v1_0/venue/search/?locality=newport%20beach&category=restaurant' \
      '&api_key=1ac07cd2c3cf46815d50a43e0707d409daa94505'

#create an object that will run the open the url



#print data['objects']

'''for item in data['objects']:
    #print " item is: " + str(item)
    print item['name']
    print item['phone']'''

# create a function that will return the restaurants and phone numbers using a location provided
def locu_search(query):
    api_key = locu_api #allocate api to a variable
    url = 'https://api.locu.com/v1_0/venue/search/?'# create a url variable
    locality = query.replace(' ', '%20') # replace space with %20 # create and clean up locality
    final_url = url + "&locality=" + locality + "&category=restaurant&" + "api_key=" + api_key # create final url
    json_obj = urllib2.urlopen(final_url)# create a json object using urllib2 to open a website
    data = json.load(json_obj) # load the json data from the opened website
    for item in data['objects']: # look up key value pairs in dictionaries
        #print " item is: " + str(item)
        print item['name'], item['phone']

locu_search('new jersey')

