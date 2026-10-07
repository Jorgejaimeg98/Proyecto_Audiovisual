from models.pelicula import Pelicula


class PeliculaDocumental(Pelicula):
    def __init__(self, id_contenido, titulo, anio_prod, duracion_min, genero,
                 idioma_orig, pais_origen, sinopsis, clasificion_edad, fecha_agg, director,
                 reparto_principal, productora, presupuesto, recaudacion,
                 rating, num_votos, formato, subtitulos_disp, audio_disp, tema_principal,
                 narrador, fuentes_inv, entrevistados, locaciones, archivo_his, org_patrocinadora,
                 premios_doc, subtitulos_descrip, objetividad):
        super().__init__(id_contenido, titulo, anio_prod, duracion_min, genero,
                 idioma_orig, pais_origen, sinopsis, clasificion_edad, fecha_agg, director,
                 reparto_principal, productora, presupuesto, recaudacion,
                 rating, num_votos, formato, subtitulos_disp, audio_disp)

        self.tema_principal = tema_principal
        self.narrador = narrador
        self.fuentes_inv = fuentes_inv
        self.entrevistados = entrevistados
        self.locaciones = locaciones
        self.archivo_his = archivo_his
        self.org_patrocinadora = org_patrocinadora
        self.premios_doc = premios_doc
        self.subtitulos_descrip = subtitulos_descrip
        self.objetividad = objetividad