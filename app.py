import urllib.request, json
endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'
api_key = 'AIzaSyBBBgQibG-Rv-w8FVzDCKHrc8vWKiFau4w'
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')
nav_drive_request = 'origins={}&destinations={}&mode=driving&key={}'.format(origin,destination,api_key)
nav_transit_request = 'origin={}&destinations={}&mode=transit&key={}'.format(origin,destination,api_key)
drive_request = endpoint + nav_drive_request
transit_request = endpoint + nav_transit_request
drive_response = urllib.request.urlopen(drive_request).read()
transit_response = urllib.request.urlopen(transit_request).read()
drive_directions = json.loads(response)
drive_time = drive_directions["rows"][0]["elements"][0]["duration"]["value"]
transit_time = transit_directions["rows"][0]["elements"][0]["duration"]["value"]
if int(drive_time) < int(transit_time):
    return("have fun in traffic")
else:
    return ("have fun waiting on the train")
