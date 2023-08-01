from urllib.request import urlopen, Request
from urllib import parse
import os

import requests

SENSIBILIDAD_PREFIJO_SUFIJO = 8
OUTPUT = "\\Desktop\\NombresEpisodios.txt"
EXTENSION_VIDEO = ".mkv"

link = input("Link de la página con el nombre de los episodios: ")
# link="https://haikyuu.fandom.com/es/wiki/Lista_de_Episodios"
tituloAntiguo = input("Título del archivo de video a reemplazar con el número del episodio escrito como una 'X' mayúscula (Ej: Episodio XX): ")
# tituloAntiguo="Episodio XX"

# r = Request(str(link.encode("UTF-8"))[2:-1], headers={'User-Agent': 'Mozilla/5.0'})
r = requests.get(link)
response = r.text   # Leer el documento html
docHTMLprincipal = response.split("\n")         # Dividir el html en líneas

primerEp = input("Escribe el nombre EXACTO del primer episodio que está en la página: ")
# primerEp="Finales y Comienzos"
segundoEp = input("Por último, escribe el nombre EXACTO del segundo episodio que está en la página: ")
# segundoEp="Club de Voleibol de la Preparatoria Karasuno"

lineaUno = 0
while not(primerEp in "".join(docHTMLprincipal[lineaUno].rstrip().lstrip())) and lineaUno < len(docHTMLprincipal)-1:
    lineaUno = lineaUno + 1   # Número de línea del 1er episodio

lineaDos = lineaUno
while not(segundoEp in "".join(docHTMLprincipal[lineaDos].rstrip().lstrip())) and lineaDos < len(docHTMLprincipal)-1:
    lineaDos = lineaDos + 1 # Número de línea del 2o episodio

if lineaUno == len(docHTMLprincipal)-1 or lineaDos == len(docHTMLprincipal)-1:    # Si no existen los títulos escritos...
    exit("Error: Nombres de episodios 1/2 inválidos")
else:
    print("Episodios 1 y 2... encontrados correctamente")

# Si los prefijos/sufijos de los episodios 1 y 2 no coinciden...
preSufCorrecto = False
while not preSufCorrecto:
    if ("".join(docHTMLprincipal[lineaUno].rstrip().lstrip())["".join(docHTMLprincipal[lineaUno].rstrip().lstrip()).index(primerEp)-SENSIBILIDAD_PREFIJO_SUFIJO:"".join(docHTMLprincipal[lineaUno].rstrip().lstrip()).index(primerEp)]
            != "".join(docHTMLprincipal[lineaDos].rstrip().lstrip())["".join(docHTMLprincipal[lineaDos].rstrip().lstrip()).index(segundoEp)-SENSIBILIDAD_PREFIJO_SUFIJO:"".join(docHTMLprincipal[lineaDos].rstrip().lstrip()).index(segundoEp)]
            or "".join(docHTMLprincipal[lineaUno].rstrip().lstrip())["".join(docHTMLprincipal[lineaUno].rstrip().lstrip()).index(primerEp)+len(primerEp):"".join(docHTMLprincipal[lineaUno].rstrip().lstrip()).index(primerEp)+len(primerEp)+SENSIBILIDAD_PREFIJO_SUFIJO]
            != "".join(docHTMLprincipal[lineaDos].rstrip().lstrip())["".join(docHTMLprincipal[lineaDos].rstrip().lstrip()).index(segundoEp)+len(segundoEp):"".join(docHTMLprincipal[lineaDos].rstrip().lstrip()).index(segundoEp)+len(segundoEp)+SENSIBILIDAD_PREFIJO_SUFIJO]):
        if SENSIBILIDAD_PREFIJO_SUFIJO > 2:
            SENSIBILIDAD_PREFIJO_SUFIJO = SENSIBILIDAD_PREFIJO_SUFIJO - 1
            print("Sensibilidad de prefijo y sufijo incorrecta, bajando sensibilidad a", SENSIBILIDAD_PREFIJO_SUFIJO)
        else:
            exit("Error: Sensibilidad de prefijo y sufijo inválida")
    else:
        print("Prefijación y sufijación de los episodios... obtenidos correctamente")
        preSufCorrecto = True

prefijo = "".join(docHTMLprincipal[lineaUno].rstrip().lstrip())["".join(docHTMLprincipal[lineaUno].rstrip().lstrip()).index(primerEp)-SENSIBILIDAD_PREFIJO_SUFIJO:"".join(docHTMLprincipal[lineaUno].rstrip().lstrip()).index(primerEp)]
sufijo = "".join(docHTMLprincipal[lineaUno].rstrip().lstrip())["".join(docHTMLprincipal[lineaUno].rstrip().lstrip()).index(primerEp)+len(primerEp):"".join(docHTMLprincipal[lineaUno].rstrip().lstrip()).index(primerEp)+len(primerEp)+SENSIBILIDAD_PREFIJO_SUFIJO]

# Sumamos la diferencia entre lineaDos y lineaUno a lineaDos para saber la línea del episodio tres
difLineas = lineaDos - lineaUno
parar = False
lineaActual = lineaDos
numEp = 2

# Escribimos el primer episodio y el segundo en el archivo
f = open(os.environ["HOMEPATH"] + OUTPUT, 'w')
print("Archivo localizado en " + OUTPUT + " se ha abierto para su escritura")
f.write(tituloAntiguo[0:tituloAntiguo.index("XX")] + "01" + tituloAntiguo[tituloAntiguo.index("XX")+2:len(tituloAntiguo)] + EXTENSION_VIDEO)
f.write("|01 - " + primerEp + EXTENSION_VIDEO + "\n")
f.write(tituloAntiguo[0:tituloAntiguo.index("XX")] + "02" + tituloAntiguo[tituloAntiguo.index("XX")+2:len(tituloAntiguo)] + EXTENSION_VIDEO)
f.write("|02 - " + segundoEp + EXTENSION_VIDEO + "\n")


while not parar: # Mientras no se haya llegado al último episodio...
    lineaActual = lineaActual + difLineas
    numEp = numEp + 1
    try:
        principio = "".join(docHTMLprincipal[lineaActual].rstrip().lstrip()).index(prefijo) # Buscamos la existencia del prefijo y del sufijo
        final = "".join(docHTMLprincipal[lineaActual].rstrip().lstrip()).index(sufijo)
        print("Episodio " + str(numEp) + " encontrado... ", end="") # Si existen significa que se ha encontrado un episodio
        nombreEp = "".join(docHTMLprincipal[lineaActual].rstrip().lstrip())[
              "".join(docHTMLprincipal[lineaActual].rstrip().lstrip()).index(prefijo)+SENSIBILIDAD_PREFIJO_SUFIJO:"".join(
                  docHTMLprincipal[lineaActual].rstrip().lstrip()).index(sufijo)]
        print(nombreEp)

        f.write(tituloAntiguo[0:tituloAntiguo.index("XX")] + "{:02d}".format(numEp) + tituloAntiguo[tituloAntiguo.index("XX")+2:len(tituloAntiguo)] + EXTENSION_VIDEO)
        f.write("|" + "{:02d}".format(numEp) + " - " + nombreEp + EXTENSION_VIDEO)

        "".join(docHTMLprincipal[lineaActual+difLineas].rstrip().lstrip()).index(prefijo)  # Buscamos la existencia del prefijo y del sufijo en el siguiente episodio
        "".join(docHTMLprincipal[lineaActual+difLineas].rstrip().lstrip()).index(sufijo)
        f.write("\n")   # Solo se ejecuta este código si no ha sido el último episodio

    except: # Si no se encuentra el prefijo o el sufijo generará un error
        print("Búsqueda terminada: no se han encontrado más episodios")
        parar = True

f.close()
print("Archivo para escritura cerrado, comprueba que esté todo bien")