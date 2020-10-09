# Lo que vamos a hacer aca es bajarnos
# el codigo fuente de nuestra pagina web

# Arrancamos por importar la libreria urllib y request!

import urllib.request

# creamos una variales para abrir el sitio web
openWeb = urllib.request.urlopen('https://www.thestartingdev.org')

# Creamos una variable para guardar y leer
# todo el contenido del sitio web que ya nos bajamos
website = openWeb.read().decode('utf-8')

# Momento de la verdad! ahora imprimimos el codigo
print(website)