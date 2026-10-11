def generar_id(base, clave_contador):
    base[clave_contador] += 1
    return base[clave_contador]