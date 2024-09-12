from datetime import date
from Asignatura import Asignatura
from Estudiante import Estudiante
from Periodo import Periodo
from Nivel import Nivel

class Matricula:
    def __init__(self, id, periodo, estudiante, active):
        self.id = id
        self.periodo = periodo
        self.estudiante = estudiante
        self.detalleMatricula = []
        self.fecha_creacion = date.today()
        self.active = active

    def addMatricula(self, detalle):
        self.detalleMatricula.append(detalle)

    def get_json(self):
        return {
            'id': self.id,
            'periodo': self.periodo,
            'estudiante': self.estudiante,
            'detalleMatricula': [d.get_json() for d in self.detalleMatricula],
            'fecha_creacion': self.fecha_creacion.isoformat(),
            'active': self.active
        }

    def validate(self):
        """Valida que el período, estudiante y detalles de la matrícula existen."""
        valid = True
        # Verificar existencia del período
        periodo_obj = Periodo.read(self.periodo)
        if periodo_obj is None:
            print(f"El periodo con ID {self.periodo} no existe.")
            valid = False

        # Verificar existencia del estudiante
        estudiante_obj = Estudiante.read(self.estudiante)
        if estudiante_obj is None:
            print(f"El estudiante con ID {self.estudiante} no existe.")
            valid = False

        # Verificar existencia de cada detalle de matrícula
        for detalle in self.detalleMatricula:
            asignatura_obj = Asignatura.read(detalle.asignatura)
            if asignatura_obj is None:
                print(f"La asignatura con ID {detalle.asignatura} no existe.")
                valid = False
            nivel_obj = Nivel.read(detalle.curso)
            if nivel_obj is None:
                print(f"El curso con ID {detalle.curso} no existe.")
                valid = False

        return valid

class DetalleMatricula:
    def __init__(self, id, asignatura, curso):
        self.id = id
        self.asignatura = asignatura
        self.curso = curso

    def get_json(self):
        return {
            'id': self.id,
            'asignatura': self.asignatura,
            'curso': self.curso
        }
