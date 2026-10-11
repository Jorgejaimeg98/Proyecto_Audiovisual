import json
import os


#Variable global
RUTA = "data/db.json"

DATOS_INICIALIZADOS = {
            "ultimo_id_contenido": 0,
            "ultimo_id_pelicula": 0,
            "ultimo_id_documental": 0,
            "ultimo_id_premium": 0,
            "ultimo_id_estreno": 0,
            "contenidos": [],
            "peliculas": [],
            "peliculas_documentales": [],
            "peliculas_premium": [],
            "peliculas_estreno": []
        }

## Función para cargar/leer la data
def cargar():
    ## excepciones para combatir los errores
    ## utf-8: es para guardar la información de escritura: í, ñ
    try:
        with open(RUTA, "r", encoding="utf-8") as archivo:
            ## load sin (s) para cargar toda la información que está en el archivo
            return json.load(archivo)
    except FileNotFoundError:
        guardar(DATOS_INICIALIZADOS)
        ## En el caso de ocurrir un error se inicializa desde 0 el archivo .json
        return DATOS_INICIALIZADOS


# Función para guardar/almacenar la data
def guardar(datos):
    directorio = os.path.dirname(RUTA)

    if directorio:
        os.makedirs(directorio, exist_ok=True)
    # open recibe 3 parámetros principales, RUTA, el modo, y la codificación
    ## w escritura, sirve para crear
    with open(RUTA, "w", encoding="utf-8") as archivo:
        # Los datos del objeto, se debe guardar en el archivo, con una determinada indentación y respetando caracteres especiales
        json.dump(datos, archivo, indent=4, ensure_ascii=False)