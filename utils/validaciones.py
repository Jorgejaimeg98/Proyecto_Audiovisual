def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None:
                if valor < minimo:
                    print(f"El valor debe ser mayor o igual a {minimo}.")
                    continue
            return valor
        except ValueError as e:
            print(f"Entrada inválida. Ingrese un número entero. {e}")


def leer_flotante(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None:
                if valor < minimo:
                    print(f"El valor debe ser mayor o igual a {minimo}.")
                    continue
            return valor
        except ValueError as e:
            print(f"Entrada inválida. Ingrese un número decimal válido. {e}")


def leer_booleano(mensaje):
    while True:
        try:
            entrada = input(f"{mensaje} (s/n): ").strip().lower()
            if entrada == "s" or entrada == "si" or entrada == "sí":
                return True
            elif entrada == "n" or entrada == "no":
                return False
            else:
                raise ValueError("Solo se permite 's' para Sí o 'n' para No.")
        except ValueError as e:
            print(f"Opción inválida. {e}")


def leer_texto(mensaje):
    while True:
        try:
            entrada = input(mensaje).strip()
            if entrada == "":
                raise ValueError("El texto no puede estar vacío.")
            return entrada
        except ValueError as e:
            print(f"Entrada inválida. {e}")