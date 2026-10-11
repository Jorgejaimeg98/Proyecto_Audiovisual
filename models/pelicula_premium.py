# CLASE 4: Segunda clase hija que hereda de Pelicula
from models.pelicula import Pelicula


class PeliculaPremium(Pelicula):
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
        precio_alquiler_base,
        dias_validez_alquiler,
        plan_minimo_requerido,
        permite_descarga_offline,
        soporte_hdr,
        cantidad_pantallas_simultaneas,
        tasa_descuento_suscripcion,
        region_restringida,
        calidad_audio_espacial,
        licencia_drm
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
        self.precio_alquiler_base = precio_alquiler_base
        self.dias_validez_alquiler = dias_validez_alquiler
        self.plan_minimo_requerido = plan_minimo_requerido  # "Standard", "VIP", "Gold"
        self.permite_descarga_offline = permite_descarga_offline
        self.soporte_hdr = soporte_hdr
        self.cantidad_pantallas_simultaneas = cantidad_pantallas_simultaneas
        self.tasa_descuento_suscripcion = tasa_descuento_suscripcion
        self.region_restringida = region_restringida
        self.calidad_audio_espacial = calidad_audio_espacial
        self.licencia_drm = licencia_drm

    def validar_acceso(self, plan_usuario):
        # Comprobación básica con if/else
        if plan_usuario == self.plan_minimo_requerido:
            return f"Acceso concedido a {self.titulo} para el plan {plan_usuario}."
        else:
            return f"Acceso denegado. Se requiere el plan {self.plan_minimo_requerido}."

    def calcular_tarifa(self, es_suscriptor):
        # Cálculo directo de descuento
        if es_suscriptor:
            descuento = self.precio_alquiler_base * (self.tasa_descuento_suscripcion / 100)
            precio_final = self.precio_alquiler_base - descuento
            return f"Precio con descuento: ${precio_final} USD."
        else:
            return f"Precio normal: ${self.precio_alquiler_base} USD."