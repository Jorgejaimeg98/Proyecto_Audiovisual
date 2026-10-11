# PROGRAMA PRINCIPAL: Consola, menús, captura de datos e invocación de servicios y métodos
from models.contenido import Contenido
from models.pelicula import Pelicula
from models.pelicula_documental import PeliculaDocumental
from models.pelicula_premium import PeliculaPremium
from models.pelicula_estreno import PeliculaEstreno

import services.contenido_service as contenido_srv
import services.pelicula_service as pelicula_srv
import services.pelicula_documental_service as documental_srv
import services.pelicula_premium_service as premium_srv
import services.pelicula_estreno_service as estreno_srv

from utils.validaciones import leer_entero, leer_flotante, leer_booleano, leer_texto


# ==============================================================================
# SUBMENÚ 1: CONTENIDO (CLASE SUPERIOR)
# ==============================================================================
def pedir_datos_contenido():
    return {
        "titulo": leer_texto("Título: "),
        "sinopsis": leer_texto("Sinopsis: "),
        "idioma_original": leer_texto("Idioma original: "),
        "pais_origen": leer_texto("País de origen: "),
        "clasificacion_edad": leer_texto("Clasificación de edad (ej. +13, +18): "),
        "duracion_minutos": leer_entero("Duración en minutos: ", minimo=1),
        "ano_lanzamiento": leer_entero("Año de lanzamiento: ", minimo=1895),
        "disponible": leer_booleano("¿Está disponible actualmente?"),
        "visualizaciones": leer_entero("Cantidad inicial de visualizaciones: ", minimo=0),
        "calificacion_base": leer_flotante("Calificación base (0.0 a 5.0): ", minimo=0.0)
    }


def instanciar_contenido(d):
    return Contenido(
        d["id_contenido"],
        d["titulo"],
        d["sinopsis"],
        d["idioma_original"],
        d["pais_origen"],
        d["clasificacion_edad"],
        d["duracion_minutos"],
        d["ano_lanzamiento"],
        d["disponible"],
        d["visualizaciones"],
        d["calificacion_base"]
    )


def subMenuContenido():
    while True:
        print("\n--- Submenú de Contenido (Clase 1) ---")
        print("1. Crear Contenido")
        print("2. Listar Contenidos")
        print("3. Actualizar Contenido")
        print("4. Eliminar Contenido")
        print("5. Registrar visualización (Método propio 1)")
        print("6. Cambiar disponibilidad (Método propio 2)")
        print("7. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            datos = pedir_datos_contenido()
            exito, nuevo_id = contenido_srv.crear(datos)
            if exito:
                print(f"Contenido creado exitosamente con ID: {nuevo_id}")
            else:
                print("Error al guardar el contenido.")

        elif opcion == "2":
            registros = contenido_srv.listar()
            if not registros:
                print("No hay contenidos registrados.")
            for registro in registros:
                print(registro)

        elif opcion == "3":
            id_buscado = leer_entero("Ingrese ID del contenido a actualizar: ", minimo=1)
            existente = contenido_srv.buscar_por_id(id_buscado)
            if existente:
                print("Ingrese los nuevos datos:")
                nuevos = pedir_datos_contenido()
                if contenido_srv.actualizar(id_buscado, nuevos):
                    print("Contenido actualizado exitosamente.")
                else:
                    print("Error al actualizar.")
            else:
                print("El ID no existe.")

        elif opcion == "4":
            id_buscado = leer_entero("Ingrese ID del contenido a eliminar: ", minimo=1)
            if contenido_srv.eliminar(id_buscado):
                print("Contenido eliminado exitosamente.")
            else:
                print("No se encontró el registro con dicho ID.")

        elif opcion == "5":
            id_buscado = leer_entero("Ingrese ID del contenido: ", minimo=1)
            registro = contenido_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_contenido(registro)
                cantidad = leer_entero("¿Cuántas visualizaciones desea agregar?: ", minimo=1)
                resultado = obj.registrar_visualizacion(cantidad)
                print(resultado)
                # Guardamos el cambio en la persistencia
                registro["visualizaciones"] = obj.visualizaciones
                contenido_srv.actualizar(id_buscado, registro)
            else:
                print("Contenido no encontrado.")

        elif opcion == "6":
            id_buscado = leer_entero("Ingrese ID del contenido: ", minimo=1)
            registro = contenido_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_contenido(registro)
                nuevo_estado = leer_booleano("¿Desea dejarlo Disponible?")
                resultado = obj.cambiar_disponibilidad(nuevo_estado)
                print(resultado)
                # Guardamos el cambio en la persistencia
                registro["disponible"] = obj.disponible
                contenido_srv.actualizar(id_buscado, registro)
            else:
                print("Contenido no encontrado.")

        elif opcion == "7":
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 7.")


# ==============================================================================
# SUBMENÚ 2: PELÍCULA (CLASE HIJA)
# ==============================================================================
def pedir_datos_pelicula():
    datos = pedir_datos_contenido()
    datos.update({
        "director": leer_texto("Director: "),
        "productora": leer_texto("Productora: "),
        "genero_principal": leer_texto("Género principal: "),
        "presupuesto_usd": leer_flotante("Presupuesto (USD): ", minimo=0.00),
        "recaudacion_usd": leer_flotante("Recaudación (USD): ", minimo=0.00),
        "resolucion_maxima": leer_texto("Resolución máxima (ej. 4K, 1080p): "),
        "tiene_subtitulos": leer_booleano("¿Tiene subtítulos?"),
        "cantidad_criticas": leer_entero("Cantidad de críticas recibidas: ", minimo=0),
        "suma_calificaciones": leer_flotante("Suma total de calificaciones: ", minimo=0.0),
        "formato_audio": leer_texto("Formato de audio (ej. Dolby Atmos 5.1): ")
    })
    return datos


def instanciar_pelicula(d):
    return Pelicula(
        d["id_contenido"], d["titulo"], d["sinopsis"], d["idioma_original"],
        d["pais_origen"], d["clasificacion_edad"], d["duracion_minutos"],
        d["ano_lanzamiento"], d["disponible"], d["visualizaciones"],
        d["calificacion_base"], d["director"], d["productora"],
        d["genero_principal"], d["presupuesto_usd"], d["recaudacion_usd"],
        d["resolucion_maxima"], d["tiene_subtitulos"], d["cantidad_criticas"],
        d["suma_calificaciones"], d["formato_audio"]
    )


def subMenuPelicula():
    while True:
        print("\n--- Submenú de Película (Clase 2) ---")
        print("1. Crear Película")
        print("2. Listar Películas")
        print("3. Actualizar Película")
        print("4. Eliminar Película")
        print("5. Registrar calificación (Método propio 1)")
        print("6. Calcular promedio (Método propio 2)")
        print("7. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            datos = pedir_datos_pelicula()
            exito, nuevo_id = pelicula_srv.crear(datos)
            if exito:
                print(f"Película guardada con ID: {nuevo_id}")
            else:
                print("Error al guardar la película.")

        elif opcion == "2":
            registros = pelicula_srv.listar()
            if not registros:
                print("No hay películas registradas.")
            for registro in registros:
                print(registro)

        elif opcion == "3":
            id_buscado = leer_entero("Ingrese ID de la película a actualizar: ", minimo=1)
            if pelicula_srv.buscar_por_id(id_buscado):
                nuevos = pedir_datos_pelicula()
                if pelicula_srv.actualizar(id_buscado, nuevos):
                    print("Película actualizada correctamente.")
                else:
                    print("Error al actualizar.")
            else:
                print("El ID no existe.")

        elif opcion == "4":
            id_buscado = leer_entero("Ingrese ID de la película a eliminar: ", minimo=1)
            if pelicula_srv.eliminar(id_buscado):
                print("Película eliminada correctamente.")
            else:
                print("Película no encontrada.")

        elif opcion == "5":
            id_buscado = leer_entero("Ingrese ID de la película: ", minimo=1)
            registro = pelicula_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_pelicula(registro)
                nota = leer_flotante("Ingrese nota de calificación (1.0 a 5.0): ", minimo=1.0)
                resultado = obj.registrar_calificacion(nota)
                print(resultado)
                registro["cantidad_criticas"] = obj.cantidad_criticas
                registro["suma_calificaciones"] = obj.suma_calificaciones
                pelicula_srv.actualizar(id_buscado, registro)
            else:
                print("Película no encontrada.")

        elif opcion == "6":
            id_buscado = leer_entero("Ingrese ID de la película: ", minimo=1)
            registro = pelicula_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_pelicula(registro)
                print(obj.calcular_promedio())
            else:
                print("Película no encontrada.")

        elif opcion == "7":
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 7.")


# ==============================================================================
# SUBMENÚ 3: PELÍCULA DOCUMENTAL (CLASE 3)
# ==============================================================================
def pedir_datos_documental():
    datos = pedir_datos_pelicula()
    datos.update({
        "tematica_investigacion": leer_texto("Temática de investigación: "),
        "fuente_historica_principal": leer_texto("Fuente histórica principal: "),
        "institucion_respaldo": leer_texto("Institución de respaldo: "),
        "es_hecho_real": leer_booleano("¿Está basado en hechos reales?"),
        "numero_entrevistados": leer_entero("Número de entrevistados: ", minimo=0),
        "rigor_academico": leer_flotante("Rigor académico (1 a 10): ", minimo=1.0),
        "locacion_principal": leer_texto("Locación principal de rodaje: "),
        "asesor_cientifico": leer_texto("Nombre del asesor científico: "),
        "archivo_multimedia_usado": leer_texto("Tipo de material de archivo usado: "),
        "impacto_social_estimado": leer_flotante("Impacto social estimado (1 a 10): ", minimo=1.0)
    })
    return datos


def instanciar_documental(d):
    return PeliculaDocumental(
        d["id_contenido"], d["titulo"], d["sinopsis"], d["idioma_original"],
        d["pais_origen"], d["clasificacion_edad"], d["duracion_minutos"],
        d["ano_lanzamiento"], d["disponible"], d["visualizaciones"],
        d["calificacion_base"], d["director"], d["productora"],
        d["genero_principal"], d["presupuesto_usd"], d["recaudacion_usd"],
        d["resolucion_maxima"], d["tiene_subtitulos"], d["cantidad_criticas"],
        d["suma_calificaciones"], d["formato_audio"],
        d["tematica_investigacion"], d["fuente_historica_principal"],
        d["institucion_respaldo"], d["es_hecho_real"], d["numero_entrevistados"],
        d["rigor_academico"], d["locacion_principal"], d["asesor_cientifico"],
        d["archivo_multimedia_usado"], d["impacto_social_estimado"]
    )


def subMenuDocumental():
    while True:
        print("\n--- Submenú de Película Documental (Clase 3) ---")
        print("1. Crear Documental")
        print("2. Listar Documentales")
        print("3. Actualizar Documental")
        print("4. Eliminar Documental")
        print("5. Registrar temática (Método propio 1)")
        print("6. Calcular valoración documental (Método propio 2)")
        print("7. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            datos = pedir_datos_documental()
            exito, nuevo_id = documental_srv.crear(datos)
            if exito:
                print(f"Documental guardado con ID: {nuevo_id}")
            else:
                print("Error al guardar el documental.")

        elif opcion == "2":
            registros = documental_srv.listar()
            if not registros:
                print("No hay documentales registrados.")
            for registro in registros:
                print(registro)

        elif opcion == "3":
            id_buscado = leer_entero("Ingrese ID del documental a actualizar: ", minimo=1)
            if documental_srv.buscar_por_id(id_buscado):
                nuevos = pedir_datos_documental()
                if documental_srv.actualizar(id_buscado, nuevos):
                    print("Documental actualizado correctamente.")
                else:
                    print("Error al actualizar.")
            else:
                print("El ID no existe.")

        elif opcion == "4":
            id_buscado = leer_entero("Ingrese ID del documental a eliminar: ", minimo=1)
            if documental_srv.eliminar(id_buscado):
                print("Documental eliminado correctamente.")
            else:
                print("Documental no encontrado.")

        elif opcion == "5":
            id_buscado = leer_entero("Ingrese ID del documental: ", minimo=1)
            registro = documental_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_documental(registro)
                nueva_tematica = leer_texto("Nueva temática: ")
                nuevo_asesor = leer_texto("Nuevo asesor científico: ")
                resultado = obj.registrar_tematica(nueva_tematica, nuevo_asesor)
                print(resultado)
                registro["tematica_investigacion"] = obj.tematica_investigacion
                registro["asesor_cientifico"] = obj.asesor_cientifico
                documental_srv.actualizar(id_buscado, registro)
            else:
                print("Documental no encontrado.")

        elif opcion == "6":
            id_buscado = leer_entero("Ingrese ID del documental: ", minimo=1)
            registro = documental_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_documental(registro)
                print(obj.calcular_valoracion_documental())
            else:
                print("Documental no encontrado.")

        elif opcion == "7":
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 7.")


# ==============================================================================
# SUBMENÚ 4: PELÍCULA PREMIUM (CLASE 4)
# ==============================================================================
def pedir_datos_premium():
    datos = pedir_datos_pelicula()
    datos.update({
        "precio_alquiler_base": leer_flotante("Precio base de alquiler (USD): ", minimo=0.0),
        "dias_validez_alquiler": leer_entero("Días de validez del alquiler: ", minimo=1),
        "plan_minimo_requerido": leer_texto("Plan mínimo requerido (Basico/Standard/VIP/Gold): "),
        "permite_descarga_offline": leer_booleano("¿Permite descarga offline?"),
        "soporte_hdr": leer_booleano("¿Tiene soporte HDR?"),
        "cantidad_pantallas_simultaneas": leer_entero("Pantallas simultáneas permitidas: ", minimo=1),
        "tasa_descuento_suscripcion": leer_flotante("Porcentaje de descuento para suscriptores (%): ", minimo=0.0),
        "region_restringida": leer_texto("Región con restricción de emisión: "),
        "calidad_audio_espacial": leer_texto("Calidad de audio espacial: "),
        "licencia_drm": leer_texto("Código de licencia DRM: ")
    })
    return datos


def instanciar_premium(d):
    return PeliculaPremium(
        d["id_contenido"], d["titulo"], d["sinopsis"], d["idioma_original"],
        d["pais_origen"], d["clasificacion_edad"], d["duracion_minutos"],
        d["ano_lanzamiento"], d["disponible"], d["visualizaciones"],
        d["calificacion_base"], d["director"], d["productora"],
        d["genero_principal"], d["presupuesto_usd"], d["recaudacion_usd"],
        d["resolucion_maxima"], d["tiene_subtitulos"], d["cantidad_criticas"],
        d["suma_calificaciones"], d["formato_audio"],
        d["precio_alquiler_base"], d["dias_validez_alquiler"],
        d["plan_minimo_requerido"], d["permite_descarga_offline"],
        d["soporte_hdr"], d["cantidad_pantallas_simultaneas"],
        d["tasa_descuento_suscripcion"], d["region_restringida"],
        d["calidad_audio_espacial"], d["licencia_drm"]
    )


def subMenuPremium():
    while True:
        print("\n--- Submenú de Película Premium (Clase 4) ---")
        print("1. Crear Película Premium")
        print("2. Listar Películas Premium")
        print("3. Actualizar Película Premium")
        print("4. Eliminar Película Premium")
        print("5. Validar acceso (Método propio 1)")
        print("6. Calcular tarifa (Método propio 2)")
        print("7. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            datos = pedir_datos_premium()
            exito, nuevo_id = premium_srv.crear(datos)
            if exito:
                print(f"Película Premium guardada con ID: {nuevo_id}")
            else:
                print("Error al guardar la película premium.")

        elif opcion == "2":
            registros = premium_srv.listar()
            if not registros:
                print("No hay películas premium registradas.")
            for registro in registros:
                print(registro)

        elif opcion == "3":
            id_buscado = leer_entero("Ingrese ID de la película premium a actualizar: ", minimo=1)
            if premium_srv.buscar_por_id(id_buscado):
                nuevos = pedir_datos_premium()
                if premium_srv.actualizar(id_buscado, nuevos):
                    print("Película Premium actualizada correctamente.")
                else:
                    print("Error al actualizar.")
            else:
                print("El ID no existe.")

        elif opcion == "4":
            id_buscado = leer_entero("Ingrese ID de la película premium a eliminar: ", minimo=1)
            if premium_srv.eliminar(id_buscado):
                print("Película Premium eliminada correctamente.")
            else:
                print("Película Premium no encontrada.")

        elif opcion == "5":
            id_buscado = leer_entero("Ingrese ID de la película premium: ", minimo=1)
            registro = premium_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_premium(registro)
                plan = leer_texto("Ingrese el plan del usuario (Basico/Standard/VIP/Gold): ")
                print(obj.validar_acceso(plan))
            else:
                print("Película premium no encontrada.")

        elif opcion == "6":
            id_buscado = leer_entero("Ingrese ID de la película premium: ", minimo=1)
            registro = premium_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_premium(registro)
                suscriptor = leer_booleano("¿El usuario posee suscripción activa?")
                print(obj.calcular_tarifa(suscriptor))
            else:
                print("Película premium no encontrada.")

        elif opcion == "7":
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 7.")


# ==============================================================================
# SUBMENÚ 5: PELÍCULA ESTRENO (CLASE 5)
# ==============================================================================
def pedir_datos_estreno():
    datos = pedir_datos_premium()
    datos.update({
        "fecha_estreno_oficial": leer_texto("Fecha de estreno oficial (AAAA-MM-DD): "),
        "recargo_taquilla": leer_flotante("Recargo de taquilla especial (USD): ", minimo=0.0),
        "es_acceso_anticipado": leer_booleano("¿Es pase de acceso anticipado?"),
        "dias_en_cartelera": leer_entero("Días transcurridos en cartelera: ", minimo=0),
        "limite_preventas": leer_entero("Límite de preventas: ", minimo=1),
        "preventas_realizadas": leer_entero("Preventas realizadas hasta hoy: ", minimo=0),
        "cadena_cine_asociada": leer_texto("Cadena de cine aliada: "),
        "evento_alfombra_roja": leer_booleano("¿Incluye evento de alfombra roja digital?"),
        "tiempo_exclusividad_dias": leer_entero("Días de exclusividad en la plataforma: ", minimo=1),
        "trailer_exclusivo_url": leer_texto("URL del trailer exclusivo: ")
    })
    return datos


def instanciar_estreno(d):
    return PeliculaEstreno(
        d["id_contenido"], d["titulo"], d["sinopsis"], d["idioma_original"],
        d["pais_origen"], d["clasificacion_edad"], d["duracion_minutos"],
        d["ano_lanzamiento"], d["disponible"], d["visualizaciones"],
        d["calificacion_base"], d["director"], d["productora"],
        d["genero_principal"], d["presupuesto_usd"], d["recaudacion_usd"],
        d["resolucion_maxima"], d["tiene_subtitulos"], d["cantidad_criticas"],
        d["suma_calificaciones"], d["formato_audio"],
        d["precio_alquiler_base"], d["dias_validez_alquiler"],
        d["plan_minimo_requerido"], d["permite_descarga_offline"],
        d["soporte_hdr"], d["cantidad_pantallas_simultaneas"],
        d["tasa_descuento_suscripcion"], d["region_restringida"],
        d["calidad_audio_espacial"], d["licencia_drm"],
        d["fecha_estreno_oficial"], d["recargo_taquilla"],
        d["es_acceso_anticipado"], d["dias_en_cartelera"],
        d["limite_preventas"], d["preventas_realizadas"],
        d["cadena_cine_asociada"], d["evento_alfombra_roja"],
        d["tiempo_exclusividad_dias"], d["trailer_exclusivo_url"]
    )


def subMenuEstreno():
    while True:
        print("\n--- Submenú de Película Estreno (Clase 5) ---")
        print("1. Crear Película de Estreno")
        print("2. Listar Películas de Estreno")
        print("3. Actualizar Película de Estreno")
        print("4. Eliminar Película de Estreno")
        print("5. Calcular recargo de estreno (Método propio 1)")
        print("6. Registrar fecha de estreno (Método propio 2)")
        print("7. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            datos = pedir_datos_estreno()
            exito, nuevo_id = estreno_srv.crear(datos)
            if exito:
                print(f"Película de estreno guardada con ID: {nuevo_id}")
            else:
                print("Error al guardar el estreno.")

        elif opcion == "2":
            registros = estreno_srv.listar()
            if not registros:
                print("No hay estrenos registrados.")
            for registro in registros:
                print(registro)

        elif opcion == "3":
            id_buscado = leer_entero("Ingrese ID del estreno a actualizar: ", minimo=1)
            if estreno_srv.buscar_por_id(id_buscado):
                nuevos = pedir_datos_estreno()
                if estreno_srv.actualizar(id_buscado, nuevos):
                    print("Película de estreno actualizada correctamente.")
                else:
                    print("Error al actualizar.")
            else:
                print("El ID no existe.")

        elif opcion == "4":
            id_buscado = leer_entero("Ingrese ID del estreno a eliminar: ", minimo=1)
            if estreno_srv.eliminar(id_buscado):
                print("Película de estreno eliminada correctamente.")
            else:
                print("Estreno no encontrado.")

        elif opcion == "5":
            id_buscado = leer_entero("Ingrese ID de la película de estreno: ", minimo=1)
            registro = estreno_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_estreno(registro)
                print(obj.calcular_recargo_estreno())
            else:
                print("Película de estreno no encontrada.")

        elif opcion == "6":
            id_buscado = leer_entero("Ingrese ID de la película de estreno: ", minimo=1)
            registro = estreno_srv.buscar_por_id(id_buscado)
            if registro:
                obj = instanciar_estreno(registro)
                nueva_fecha = leer_texto("Nueva fecha de estreno (AAAA-MM-DD): ")
                resultado = obj.registrar_fecha_estreno(nueva_fecha)
                print(resultado)
                registro["fecha_estreno_oficial"] = obj.fecha_estreno_oficial
                registro["tiempo_exclusividad_dias"] = obj.tiempo_exclusividad_dias
                estreno_srv.actualizar(id_buscado, registro)
            else:
                print("Película de estreno no encontrada.")

        elif opcion == "7":
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 7.")


# ==============================================================================
# MENÚ PRINCIPAL
# ==============================================================================
def menuPrincipal():
    while True:
        print("\n=============================================")
        print("  SISTEMA DE PLATAFORMA AUDIOVISUAL (GRUPO 7)")
        print("=============================================")
        print("1. Gestionar Contenidos")
        print("2. Gestionar Películas")
        print("3. Gestionar Películas Documentales")
        print("4. Gestionar Películas Premium")
        print("5. Gestionar Películas de Estreno")
        print("6. Salir")

        opcion = input("Ingrese una de las opciones: ").strip()

        if opcion == "1":
            subMenuContenido()
        elif opcion == "2":
            subMenuPelicula()
        elif opcion == "3":
            subMenuDocumental()
        elif opcion == "4":
            subMenuPremium()
        elif opcion == "5":
            subMenuEstreno()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Ingrese un número del 1 al 6.")

menuPrincipal()