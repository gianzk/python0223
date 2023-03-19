import requests # me sirve para conectarme al sitio web
from lxml import html # para extraer texto o navegar por el arbol html

url = 'https://www.wikipedia.org/'
#url='http://www.adasdaxsaxs.com/' -> pagina incorrecta
# REQUERIMIENTO AL SERVIDOR
respuesta = requests.get(url)
print("this is response",respuesta.status_code,respuesta.url,respuesta.text)
# PARSEO DEL ARBOL HTML QUE RECIBO COMO RESPUESTA CON LXML
parser = html.fromstring(respuesta.text)

print("a un clase HTML =>",parser)

# EXTRACCION DE TODOS LOS IDIOMAS POR CLASE
idiomas = parser.find_class('central-featured-lang')
print(idiomas)

for idioma in idiomas:
    print("text=>",idioma.text_content()) 
## buscar una codificacion utf-8

