#  Kevan Hong-Nhan Nguyen 71632979.  ICS 32 Lab sec 9.  Project #3

import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'Fmjtd%7Cluu8216z2h%2C8n%3Do5-942xqz'

BASE_MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'

def build_search_url(locations: [str]) -> str:
    '''
    Takes the location queries and builds/returns a URL that can be
    used to access the directions from the starting location to the
    destination with the MapQuest API
    '''
    query_parameters = [('from', locations[0])]
    for i in range(1, len(locations)):
        query_parameters.append(('to', locations[i]))

    return BASE_MAPQUEST_URL + '/route?key=' + MAPQUEST_API_KEY + '&' + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> 'json':
    '''
    This function takes a URL and returns a Python object representing the
    parsed JSON response.
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if response != None:
            response.close()
