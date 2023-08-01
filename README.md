# Obtenedor de nombres de episodios para su renombrado
Un programa creado con la finalidad de obtener los nombres de los episodios de una serie para cambiar el nombre de los archivos de video con una herramienta que sustituya los nombres de los archivos, como por ejemplo <a href="https://www.bulkrenameutility.co.uk">Bulk Rename Utility</a>.

![image](https://github.com/Sauleteh/obtenedor-nombres-episodios-para-renombrado/assets/22859905/81ab1519-6cd3-41b7-9e6b-18104b8977e1)

## Instrucciones de uso
1. Ejecuta el archivo Python proporcionado. Recuerda instalar antes las librerías necesarias (*pip install requests*)
2. Inserta la página web donde se encuentran los nombres de los episodios. Supuestamente funciona con cualquier página, aunque no siempre. Funciona especialmente bien con Wikipedia
3. Inserta el nombre de los archivos a sustituir, cambiando el lugar donde va los episodios por un número indeterminado de caracteres 'X'. Ej: Tienes "*Serie2023ep01_1080*", "*Serie2023ep02_1080*"... entonces introduces en el programa *Serie2023ep**XX**_1080*. NO introduzcas la extensión del archivo, eso lo indicas tú en las variables que están en las primeras líneas del programa.
4. Por último, introduce el nombre del primer episodio y posteriormente el nombre del segundo. Si los nombres en la página tienen comillas o cualquier decorativo en los nombres, no hace falta que copies estos decorativos también, solo introduce el nombre del episodio, sin nada más.

Cuando el programa termine, creará un archivo de texto en el escritorio (puedes cambiar el destino en las variables del programa). Este archivo debe tener una línea por cada episodio y tiene un estilo como el siguiente: *OPM_Ep01-21.mkv|01 - El hombre más poderoso del mundo.mkv* (es decir, a la izquierda del carácter '|' el nombre original del archivo y a la derecha el nombre nuevo del archivo).

Ahora que ya tenemos el archivo, tendremos que insertarlo en un programa que se encargue de cambiar los nombres. Para ello, utilizaremos el programa *Bulk Rename Utility*:
1. Vamos a la carpeta donde estén los archivos desde el panel izquierdo
2. Importamos el archivo de texto generado anteriormente como se indica en la siguiente captura

![image](https://github.com/Sauleteh/obtenedor-nombres-episodios-para-renombrado/assets/22859905/6881c2ca-5e65-4c60-9133-dfe5e06b1209)

3. Seleccionamos todos los archivos a renombrar (*CTRL + A* en Windows para seleccionar todo) y presionamos el botón *Rename*.

En un futuro se pretende integrar en el propio programa un renombrador automático sin necesidad de usar programas externos como el usado anteriormente.
