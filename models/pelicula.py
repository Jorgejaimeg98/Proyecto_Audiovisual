from models.contenido import Contenido


class Pelicula(Contenido):
    def __init__(self,id_contenido, titulo, anio_prod, duracion_min, genero,
                 idioma_orig, pais_origen, sinopsis, clasificion_edad, fecha_agg,
                 director, reparto_principal, productora, presupuesto, recaudacion,
                 rating, num_votos, formato, subtitulos_disp, audio_disp):
        super().__init__(id_contenido, titulo, anio_prod, duracion_min, genero,
                 idioma_orig, pais_origen, sinopsis, clasificion_edad, fecha_agg)

        self.director = director
        self.reparto_principal = reparto_principal
        self.productora = productora
        self.presupuesto = presupuesto
        self.recaudacion = recaudacion
        self.rating = rating
        self.num_votos = num_votos
        self.formato = formato
        self.subtitulos_disp = subtitulos_disp
        self.audio_disp = audio_disp