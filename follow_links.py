import urllib.request
from bs4 import BeautifulSoup

# Pedir datos al usuario
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

print("Retrieving:", url)

# Repetir el proceso según el número de veces indicado
for i in range(count):
    # Leer el HTML de la página actual
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Obtener todos los enlaces <a>
    tags = soup('a')

    # Buscar el enlace en la posición especificada
    link = tags[position - 1].get('href', None)
    print("Retrieving:", link)
    
    # Actualizar la URL para la siguiente iteración
    url = link

# Mostrar el último nombre
name = url.split('_')[-1].split('.')[0]
print("The answer to the assignment for this execution is", '"' + name + '"')
