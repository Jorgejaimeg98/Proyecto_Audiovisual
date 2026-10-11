from repository import repo_json
from utils.generador_id import generar_id


def crear(datos_dict):
    try:
        base = repo_json.cargar()
        nuevo_id = generar_id(base, "ultimo_id_contenido")
        datos_dict["id_contenido"] = nuevo_id
        base["contenidos"].append(datos_dict)
        repo_json.guardar(base)
        return True, nuevo_id
    except ValueError:
        return False, None


def listar():
    base = repo_json.cargar()
    return base.get("contenidos", [])


def buscar_por_id(id_buscar):
    for item in listar():
        if item["id_contenido"] == id_buscar:
            return item
    return None


def actualizar(id_buscar, nuevos_datos):
    base = repo_json.cargar()
    for item in base["contenidos"]:
        if item["id_contenido"] == id_buscar:
            item.update(nuevos_datos)
            item["id_contenido"] = id_buscar
            repo_json.guardar(base)
            return True
    return False


def eliminar(id_buscar):
    base = repo_json.cargar()
    for item in base["contenidos"]:
        if item["id_contenido"] == id_buscar:
            base["contenidos"].remove(item)
            repo_json.guardar(base)
            return True
    return False