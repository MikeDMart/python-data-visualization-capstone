import urllib.request
import json

# Solicita la URL al usuario
url = input('Enter location: ')
print('Retrieving', url)

# Lee los datos desde la URL
data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

# Convierte el JSON a una estructura de Python (diccionario)
info = json.loads(data)

# Extrae los números y calcula la suma
counts = [item['count'] for item in info['comments']]
print('Count:', len(counts))
print('Sum:', sum(counts))
