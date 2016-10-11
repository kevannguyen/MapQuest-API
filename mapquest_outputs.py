#  Kevan Hong-Nhan Nguyen 71632979.  ICS 32 Lab sec 9.  Project #3.

####Contains all the output generator classes to display specific
####output from MapQuest, as specified by the user.

class Steps():
    '''
    Class dedicated to displaying the directions
    '''

    def __init__(self, json):
        '''
        Initialize it with the given JSON
        '''
        self._json = json

    def generate(self):
        '''
        Displays the directions of the given JSON
        '''
        print('DIRECTIONS')
        for item in self._json['route']['legs']:
            for item2 in item['maneuvers']:
                print(item2['narrative'])
        print()

                
class Distance():
    '''
    Class dedicated to displaying the total distance
    '''

    def __init__(self, json):
        '''
        Initialize it with the given JSON
        '''
        self._json = json

    def generate(self):
        '''
        Displays the total distance of the given JSON
        '''
        print('Total Distance: {:.0f} miles'.format(self._calculate_distance()))
        print()

    def _calculate_distance(self) -> float:
        '''
        Calculates the total distance of the given JSON
        '''
        total = 0
        for item in self._json['route']['legs']:
            total += item['distance']
        return total


class Time():
    '''
    Class dedicated to displaying the total time of the given JSON
    '''

    def __init__(self, json):
        '''
        Initialize it with the given JSON
        '''
        self._json = json

    def generate(self):
        '''
        Displays the total distance of the given JSON
        '''
        print('Total Time: {:.0f} minutes'.format(self._calculate_time()))
        print()

    def _calculate_time(self) -> float:
        '''
        Calculates the total time of the given JSON.
        Returns result in minutes.
        '''
        total = 0
        for item in self._json['route']['legs']:
            total += item['time']
        return total / 60


class Location():
    '''
    Class dedicated to displaying the locations of the
    given JSON in latitude and longitude
    '''

    def __init__(self, json):
        '''
        Initialize it with the given JSON
        '''
        self._json = json
        self._directions = {True: 'NE', False: 'SW'}

    def generate(self):
        '''
        Displays all of the locations in latitude/longitude
        '''
        for location in self._json['route']['locations']:
            lat = location['latLng']['lat']
            latDir = self._directions[self._pos_or_neg(lat)][0]

            lng = location['latLng']['lng']
            lngDir = self._directions[self._pos_or_neg(lng)][1]

            print('{:.2f}{} {:.2f}{}'.format(abs(lat), latDir, abs(lng), lngDir))
        print()

    def _pos_or_neg(self, coord: float):
        '''
        Returns True if given number is positive and
        False if it is negative. To be used to identify
        which direction the longitude/latitude is in.
        '''
        return coord > 0
