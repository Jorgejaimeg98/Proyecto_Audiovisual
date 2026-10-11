# CLASE 2: Hereda directamente de Contenido
from models.contenido import Contenido


class Pelicula(Contenido):
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
        calificacion_base,
        # 10 Atributos Propios
        director,
        productora,
        genero_principal,
        presupuesto_usd,
        recaudacion_usd,
        resolucion_maxima,
        tiene_subtitulos,
        cantidad_criticas,
        suma_calificaciones,
        formato_audio
    ):
        super().__init__(
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
        )
        self.director = director
        self.productora = productora
        self.genero_principal = genero_principal
        self.presupuesto_usd = presupuesto_usd
        self.recaudacion_usd = recaudacion_usd
        self.resolucion_maxima = resolucion_maxima
        self.tiene_subtitulos = tiene_subtitulos
        self.cantidad_criticas = cantidad_criticas
        self.suma_calificaciones = suma_calificaciones
        self.formato_audio = formato_audio

    def registrar_calificacion(self, nota):
        if nota < 1 or nota > 5:
            return "La calificación debe situarse entre 1 y 5 estrellas."
        self.suma_calificaciones += nota
        self.cantidad_criticas += 1
        return f"Calificación de {nota} registrada con éxito. Total críticas: {self.cantidad_criticas}."

    def calcular_promedio(self):
        if self.cantidad_criticas == 0:
            return f"'{self.titulo}' aún no cuenta con críticas registradas."
        promedio = self.suma_calificaciones / self.cantidad_criticas
        return f"Promedio de crítica para '{self.titulo}': {float(promedio):.2f} / 5.0 (sobre {self.cantidad_criticas} votos)."