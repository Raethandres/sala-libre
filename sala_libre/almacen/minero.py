from bs4 import BeautifulSoup
import requests
from models import Laboratorio

URL_BASE = "http://labcomp.unet.edu.ve/horario.php?id="
MAX_PAGES = 3

counter = 0
print("andres")
for i in range(1, MAX_PAGES):

    # Construyo la URL
    if i > 1:
        url = URL_BASE+str(i)
    else:
        url = URL_BASE+str(1)
    print(url)
    # Realizamos la petición a la web
    req = requests.get(url)
    # Comprobamos que la petición nos devuelve un Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:

        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, "html.parser")

        # Obtenemos todos los divs donde estan las entradas
        entradas = html.find_all('tr')
        s=0
        # Recorremos todas las entradas para extraer el título, autor y fecha
        for entrada in entradas:
            counter += 1
            titulo = entrada.find_all('td')
            for t in titulo:
            	x=t.getText()
            	if x == '7am-8am':
            		s=1
            	if s:
            		print(x)
            	if x == '6pm-7pm':
            		s=0

    else:
        # Si ya no existe la página y me da un 400
        break
 