# CLASE 1: Clase Superior

class Contenido:
    def __init__(
        self,
        id_contenido,
        titulo,
        sinopsis,
        idioma_original,
        pais_origen,
        clasificacion_edad,
        duracion_minutos,
        ano_lanzamiento,
        disponible,
        visualizaciones,
        calificacion_base
    ):
        # 10 Atributos Propios
        self.id_contenido = id_contenido
        self.titulo = titulo
        self.sinopsis = sinopsis
        self.idioma_original = idioma_original
        self.pais_origen = pais_origen
        self.clasificacion_edad = clasificacion_edad
        self.duracion_minutos = duracion_minutos
        self.ano_lanzamiento = ano_lanzamiento
        self.disponible = disponible                    # bool
        self.visualizaciones = visualizaciones          # int
        self.calificacion_base = calificacion_base      # float

    def registrar_visualizacion(self, cantidad):
        if not self.disponible:
            return f"El contenido '{self.titulo}' no está disponible para visualización."
        self.visualizaciones = self.visualizaciones + cantidad
        return f"Se sumaron {cantidad} visualizaciones a '{self.titulo}'. Total actual: {self.visualizaciones}."

    def cambiar_disponibilidad(self, nuevo_estado):
        self.disponible = nuevo_estado
        if self.disponible:
            estado_texto = "Disponible"
        else:
            estado_texto = "No disponible"
        return f"El estado de '{self.titulo}' ha cambiado a: {estado_texto}."