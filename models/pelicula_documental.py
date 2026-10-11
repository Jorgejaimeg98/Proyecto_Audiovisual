# CLASE 3: Primera clase hija que hereda de Pelicula
from models.pelicula import Pelicula


class PeliculaDocumental(Pelicula):
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
        director,
        productora,
        genero_principal,
        presupuesto_usd,
        recaudacion_usd,
        resolucion_maxima,
        tiene_subtitulos,
        cantidad_criticas,
        suma_calificaciones,
        formato_audio,
        # 10 Atributos Propios
        tematica_investigacion,
        fuente_historica_principal,
        institucion_respaldo,
        es_hecho_real,
        numero_entrevistados,
        rigor_academico,
        locacion_principal,
        asesor_cientifico,
        archivo_multimedia_usado,
        impacto_social_estimado
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
            calificacion_base,
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
        )
        self.tematica_investigacion = tematica_investigacion
        self.fuente_historica_principal = fuente_historica_principal
        self.institucion_respaldo = institucion_respaldo
        self.es_hecho_real = es_hecho_real
        self.numero_entrevistados = numero_entrevistados
        self.rigor_academico = rigor_academico          # Escala 1 a 10
        self.locacion_principal = locacion_principal
        self.asesor_cientifico = asesor_cientifico
        self.archivo_multimedia_usado = archivo_multimedia_usado
        self.impacto_social_estimado = impacto_social_estimado

    def registrar_tematica(self, nueva_tematica, nuevo_asesor):
        self.tematica_investigacion = nueva_tematica
        self.asesor_cientifico = nuevo_asesor
        return f"Temática actualizada a '{nueva_tematica}' bajo supervisión de {nuevo_asesor}."

    def calcular_valoracion_documental(self):
        # Promedio simple de las dos notas (de 1 a 10)
        promedio = (self.rigor_academico + self.impacto_social_estimado) / 2
        return f"Valoración del documental '{self.titulo}': {float(promedio):.1f} / 10 puntos."