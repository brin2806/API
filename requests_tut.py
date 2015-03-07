# tutorial about learning to use request module
# import the requests module

import requests

# lets get a webpage.  We create a response object called 'r'
# we can get all the info we need from this 'r' object


r = requests.get('https://api.github.com/events')

'''PASSING PARAMETERS IN URLS'''

'''
