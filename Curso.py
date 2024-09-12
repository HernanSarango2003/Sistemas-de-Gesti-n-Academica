from datetime import date

class Curso:
    def __init__(self, id, nombre, fecha_creacion=None, active=True):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion if fecha_creacion else date.today()
        self.active = active

    def get_json(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'fecha_creacion': self.fecha_creacion.isoformat(),  # Convertir la fecha a un formato de cadena
            'active': self.active
        }
