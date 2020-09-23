import requests as req

# Make a get request of the given url1
get_url = req.get("http://api.letgo.com/api/iplookup.json")

print get_url.text  # print the values text values in the url to check

# fetching the latitude and longitude values from url1
res = get_url.json()

geodata = dict()
geodata['lat'] = res['latitude']
geodata['lon'] = res['longitude']
print ("latitude : {lat}, longitude : {lon}".format(**geodata))

# replace given lat lon with the fetched value

response = req.post("https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json".format(**geodata))

print response.text  # print the json file text after modifying it

get_url2 = req.get("https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json".format(**geodata))
res2 = get_url2.json()

di_city = dict()
di_city['name'] = res2["display_name"]
di_city['city'] = res["city"]
print ("display_name: {name}, city: {city}".format(
    **di_city))  # fetch and print the display name and city from the response
