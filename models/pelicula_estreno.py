# CLASE 5: Clase hija que hereda de PeliculaPremium
from models.pelicula_premium import PeliculaPremium


class PeliculaEstreno(PeliculaPremium):
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
        precio_alquiler_base,
        dias_validez_alquiler,
        plan_minimo_requerido,
        permite_descarga_offline,
        soporte_hdr,
        cantidad_pantallas_simultaneas,
        tasa_descuento_suscripcion,
        region_restringida,
        calidad_audio_espacial,
        licencia_drm,
        # 10 Atributos Propios
        fecha_estreno_oficial,
        recargo_taquilla,
        es_acceso_anticipado,
        dias_en_cartelera,
        limite_preventas,
        preventas_realizadas,
        cadena_cine_asociada,
        evento_alfombra_roja,
        tiempo_exclusividad_dias,
        trailer_exclusivo_url
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
            formato_audio,
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
        )
        self.fecha_estreno_oficial = fecha_estreno_oficial
        self.recargo_taquilla = recargo_taquilla
        self.es_acceso_anticipado = es_acceso_anticipado
        self.dias_en_cartelera = dias_en_cartelera
        self.limite_preventas = limite_preventas
        self.preventas_realizadas = preventas_realizadas
        self.cadena_cine_asociada = cadena_cine_asociada
        self.evento_alfombra_roja = evento_alfombra_roja
        self.tiempo_exclusividad_dias = tiempo_exclusividad_dias
        self.trailer_exclusivo_url = trailer_exclusivo_url

    def calcular_recargo_estreno(self):
        # Suma directa del precio base y el recargo
        precio_total = self.precio_alquiler_base + self.recargo_taquilla
        return f"El precio final de estreno para {self.titulo} es: ${precio_total} USD."

    def registrar_fecha_estreno(self, nueva_fecha):
        # Asignación directa
        self.fecha_estreno_oficial = nueva_fecha
        return f"Fecha de estreno actualizada al {self.fecha_estreno_oficial}."


    """def calcular_recargo_estreno(self):
        total = self.precio_alquiler_base + self.recargo_taquilla
        if self.es_acceso_anticipado:
            total += 3.50  # Tarifa extra por acceso VIP anticipado
            return f"Precio total de estreno (con Acceso Anticipado VIP): ${total:.2f} USD."
        return f"Precio total de estreno: ${total:.2f} USD (Base: ${self.precio_alquiler_base:.2f} + Recargo: ${self.recargo_taquilla:.2f})."

    def registrar_fecha_estreno(self, nueva_fecha, dias_exclusividad):
        self.fecha_estreno_oficial = nueva_fecha
        self.tiempo_exclusividad_dias = dias_exclusividad
        return f"Estreno reprogramado para el {nueva_fecha} con {dias_exclusividad} días de exclusividad."""