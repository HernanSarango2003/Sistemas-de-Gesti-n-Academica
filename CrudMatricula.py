from utilss import green_color, blue_color, gotoxy, BorrarPantalla, linea
from Componets import Menu, Valida
from ClsJson import JsonFile
from Matricula import Matricula, DetalleMatricula
from Icrud import Icrud
import time
import os


path, file = os.path.split(__file__)

class CrudMatricula(Icrud):
    json_file = JsonFile(f"{path}/data/matriculas.json")

    def create(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{green_color}Registrar Matrícula")
        linea(80, green_color)
        
        matriculas = self.json_file.read()
        
        if matriculas:
            next_id = max(m['id'] for m in matriculas) + 1
        else:
            next_id = 1
        
        periodo = input(f"{blue_color}Ingrese el periodo de la matrícula: {green_color}")
        estudiante = input(f"{blue_color}Ingrese el estudiante de la matrícula: {green_color}")
        
        detalle_matricula = []
        add_details = True
        
        while add_details:
            id_detalle = len(detalle_matricula) + 1
            asignatura = input(f"{blue_color}Ingrese la asignatura: {green_color}")
            curso = input(f"{blue_color}Ingrese el curso: {green_color}")
            
            detalle = DetalleMatricula(id_detalle, asignatura, curso)
            detalle_matricula.append(detalle)
            
            more = input(f"{blue_color}¿Desea añadir otro detalle? (s/n): {green_color}")
            if more.lower() != 's':
                add_details = False

        active = True
        nueva_matricula = Matricula(next_id, periodo, estudiante, active)
        for detalle in detalle_matricula:
            nueva_matricula.addMatricula(detalle)
        
        matriculas.append(nueva_matricula.get_json())
        self.json_file.save(matriculas)
        print(f"{green_color}Matrícula registrada correctamente con ID: {blue_color}{next_id}")
        time.sleep(2)

    def update(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{green_color}Actualizar Matrícula")
        linea(80, green_color)
        
        id_matricula = int(Valida.solo_numeros(
            entrada=input(f"{blue_color}Ingrese el ID de la matrícula a actualizar: {green_color}"),
            mensaje_error="El ID debe ser un número válido",
            col=10,
            fil=10
        ))
        
        matriculas = self.json_file.read()
        matricula_encontrada = False
        for matricula in matriculas:
            if matricula["id"] == id_matricula and matricula["active"]:
                matricula_encontrada = True
                print(f"{blue_color}Matrícula encontrada: {green_color}{matricula['estudiante']}")
                
                nuevo_periodo = input(f"{blue_color}Ingrese el nuevo periodo (deje en blanco para no cambiar): {green_color}")
                nuevo_estudiante = input(f"{blue_color}Ingrese el nuevo estudiante (deje en blanco para no cambiar): {green_color}")
                
                if nuevo_periodo:
                    matricula["periodo"] = nuevo_periodo
                if nuevo_estudiante:
                    matricula["estudiante"] = nuevo_estudiante
                
                self.json_file.save(matriculas)
                print(f"{blue_color}Matrícula actualizada correctamente")
                time.sleep(2)
                break
        
        if not matricula_encontrada:
            print(f"{blue_color}La matrícula no existe o no está activa")
            time.sleep(2)

    def delete(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{green_color}Eliminar Matrícula")
        linea(80, green_color)
        
        id_matricula = int(Valida.solo_numeros(
            entrada=input(f"{blue_color}Ingrese el ID de la matrícula a eliminar: {green_color}"),
            mensaje_error="El ID debe ser un número válido",
            col=10,
            fil=10
        ))
        
        matriculas = self.json_file.read()
        matricula_encontrada = False
        for matricula in matriculas:
            if matricula["id"] == id_matricula and matricula["active"]:
                matricula_encontrada = True
                print(f"{blue_color}Matrícula encontrada: {green_color}{matricula['estudiante']}")
                confirmacion = input(f"{blue_color}¿Está seguro de eliminar la matrícula? (s/n): {green_color}")
                if confirmacion.lower() == 's':
                    matricula["active"] = False
                    self.json_file.save(matriculas)
                    print(f"{green_color}Matrícula eliminada correctamente")
                    time.sleep(2)
                else:
                    print(f"{blue_color}No se eliminó la matrícula")
                    time.sleep(2)
                break
        
        if not matricula_encontrada:
            print(f"{blue_color}La matrícula no existe o ya está inactiva")
            time.sleep(2)
    
    def consult(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{green_color}Mostrar Matrículas")
        linea(80, green_color)
        
        matriculas = self.json_file.read()
        
        menu = Menu("Seleccione una opción", ["Mostrar todas las matrículas", "Buscar matrícula por ID", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
        opc = menu.menu()
        
        if opc == '1':
            BorrarPantalla()
            linea(80, green_color)
            gotoxy(32, 2); print(f"{green_color}Todas las Matrículas")
            linea(80, green_color)
            
            if matriculas:
                matriculas_encontradas = False
                for matricula in matriculas:
                    if matricula['active']:
                        print(f"{blue_color}ID: {green_color}{matricula['id']}\n{blue_color}Estudiante: {green_color}{matricula['estudiante']}\n{blue_color}Periodo: {green_color}{matricula['periodo']}\n")
                        matriculas_encontradas = True
                if not matriculas_encontradas:
                    print(f"{green_color}No hay matrículas registradas.")
            else:
                print(f"{green_color}No hay matrículas registradas.")
            time.sleep(3)
        
        elif opc == '2':
            id_matricula = int(Valida.solo_numeros(
                entrada=input(f"{blue_color}Ingrese el ID de la matrícula a buscar: {green_color}"),
                mensaje_error="El ID debe ser un número válido",
                col=10,
                fil=10
            ))
            matriculas_encontradas = False
            for matricula in matriculas:
                if matricula['id'] == id_matricula and matricula['active']:
                    print(f"{blue_color}Matrícula encontrada: {green_color}{matricula['estudiante']}\nPeriodo: {green_color}{matricula['periodo']}")
                    matriculas_encontradas = True
                    break
            if not matriculas_encontradas:
                print(f"{blue_color}Matrícula no encontrada o inactiva")
            time.sleep(3)
