import urllib.request
import urllib.parse
import json

# Service URL
serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Prompt for location
address = input('Enter location: ')

if len(address) < 1:
    print('No address provided')
    exit()

# Encode the address parameter
params = {'q': address}
url = serviceurl + urllib.parse.urlencode(params)

print('Retrieving', url)

# Make the API request
try:
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    print('Retrieved', len(data), 'characters')
    
    # Parse JSON data
    js = json.loads(data)
    
    # Extract the first plus_code
    if 'features' in js and len(js['features']) > 0:
        plus_code = js['features'][0]['properties']['plus_code']
        print('Plus code', plus_code)
    else:
        print('No results found')
        
except Exception as e:
    print('Error:', e)