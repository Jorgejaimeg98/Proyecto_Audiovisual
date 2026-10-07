from models.pelicula import Pelicula


class PeliculaPremium(Pelicula):
    def __init__(self, id_contenido, titulo, anio_prod, duracion_min, genero,
                 idioma_orig, pais_origen, sinopsis, clasificion_edad, fecha_agg,
                 director, reparto_principal, productora, presupuesto, recaudacion,
                 rating, num_votos, formato, subtitulos_disp, audio_disp, es_premium,
                 plan_requerido, costo_alquiler, costo_compra, descarga_disp, calidad_max,
                 disp_permitidos, tiempo_alquiler, pais_disp, licencia_exp):
        super().__init__(id_contenido, titulo, anio_prod, duracion_min, genero,
                 idioma_orig, pais_origen, sinopsis, clasificion_edad, fecha_agg,
                 director, reparto_principal, productora, presupuesto, recaudacion,
                 rating, num_votos, formato, subtitulos_disp, audio_disp)

        self.es_premium = es_premium
        self.plan_requerido = plan_requerido
        self.costo_alquiler = costo_alquiler
        self.costo_compra = costo_compra
        self.descarga_disp = descarga_disp
        self.calidad_max = calidad_max
        self.disp_permitidos = disp_permitidos
        self.tiempo_alquiler = tiempo_alquiler
        self.pais_disp = pais_disp
        self.licencia_exp = licencia_exp