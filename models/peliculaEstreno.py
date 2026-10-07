from models.peliculaPremium import PeliculaPremium


class PeliculaEstreno(PeliculaPremium):
    def __init__(self, id_contenido, titulo, anio_prod, duracion_min, genero,
                 idioma_orig, pais_origen, sinopsis, clasificion_edad, fecha_agg, director,
                 reparto_principal, productora, presupuesto, recaudacion,
                 rating, num_votos, formato, subtitulos_disp, audio_disp,
                 es_premium, plan_requerido, costo_alquiler, costo_compra,
                 descarga_disp, calidad_max, disp_permitidos, tiempo_alquiler, pais_disp,
                 licencia_exp, fecha_estreno, exclusivo_plataforma, dias_en_cartelera,
                 ventana_exclusividad, paises_estreno, evento_prom, trailer_url,
                 patrocinadores, acceso_anticipado, cod_invitacion):
        super().__init__(id_contenido, titulo, anio_prod, duracion_min, genero,
                 idioma_orig, pais_origen, sinopsis, clasificion_edad, fecha_agg, director,
                 reparto_principal, productora, presupuesto, recaudacion,
                 rating, num_votos, formato, subtitulos_disp, audio_disp,
                 es_premium, plan_requerido, costo_alquiler, costo_compra,
                 descarga_disp, calidad_max, disp_permitidos, tiempo_alquiler, pais_disp,
                 licencia_exp)

        self.fecha_estreno = fecha_estreno
        self.exclusivo_plataforma = exclusivo_plataforma
        self.dias_en_cartelera = dias_en_cartelera
        self.ventana_exclusividad = ventana_exclusividad
        self.paises_estreno = paises_estreno
        self.evento_prom = evento_prom
        self.trailer_url =trailer_url
        self.patrocinadores =patrocinadores
        self.acceso_anticipado = acceso_anticipado
        self.cod_invitacion = cod_invitacion