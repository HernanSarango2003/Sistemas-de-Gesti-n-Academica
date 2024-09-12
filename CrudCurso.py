from utilss import green_color, blue_color, gotoxy, BorrarPantalla, linea
from Componets import Menu, Valida
from ClsJson import JsonFile
from Curso import Curso
from Icrud import Icrud
import time
import os
from datetime import date

path, file = os.path.split(__file__)

class CrudCurso(Icrud):
    json_file = JsonFile(f"{path}/data/cursos.json")

    def create(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{green_color}Registro de Curso")
        linea(80, green_color)
        
        cursos = self.json_file.read()
        
        if cursos:
            next_id = max(c['id'] for c in cursos) + 1
        else:
            next_id = 1
        
        nombre_curso = input(f"{blue_color}Ingrese el nombre del curso: {green_color}")
        linea(80, green_color)
        curso_existente = self.json_file.find('nombre', nombre_curso)
    
        if curso_existente:
            curso = curso_existente[0]
            print(f"{blue_color}El curso ya existe")
            print(f"{green_color}ID: {blue_color}{curso['id']}\n{green_color}Nombre: {blue_color}{curso['nombre']}")
            linea(80, green_color)
            time.sleep(2)
        else:
            linea(80, green_color)
            print(f"{green_color}Curso registrado correctamente")
            print(f"{green_color}ID: {blue_color}{next_id}\n{green_color}Nombre: {blue_color}{nombre_curso}")
            linea(80, green_color)
            nuevo_curso = Curso(next_id, nombre_curso, fecha_creacion=date.today())
            cursos.append(nuevo_curso.get_json())
            self.json_file.save(cursos)
            print(f"{green_color}Curso guardado correctamente")
            time.sleep(2)

    def update(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{green_color}Actualizar Curso")
        linea(80, green_color)
        
        id_curso_str = input(f"{blue_color}Ingrese el ID del curso a actualizar: {green_color}")
        id_curso = Valida.solo_numeros(
            entrada=id_curso_str,
            mensaje_error="El ID debe ser un número válido",
            col=10,  # Ajusta según tu diseño
            fil=10   # Ajusta según tu diseño
        )
        
        if id_curso is None:
            print(f"{blue_color}ID inválido. Regresando al menú principal.")
            time.sleep(2)
            return
        
        cursos = self.json_file.read()  
        linea(80, green_color)
        curso_encontrado = False
        for curso in cursos:
            if curso["id"] == id_curso and curso["active"]:
                curso_encontrado = True
                print(f"{blue_color}Curso encontrado: {green_color}{curso['nombre']}")
                nuevo_nombre = input(f"{blue_color}Ingrese el nuevo nombre del curso: {green_color}")
                
                duplicado = self.json_file.find('nombre', nuevo_nombre)
                
                if duplicado:
                    print(f"{green_color}El curso ya existe")
                    time.sleep(2)
                    return
                
                confirmacion = input(f"{blue_color}¿Está seguro de actualizar el curso? s/n: {green_color}")
                if confirmacion.lower() == 's':
                    curso["nombre"] = nuevo_nombre
                    self.json_file.save(cursos)
                    print(f"{blue_color}Curso actualizado correctamente")
                    time.sleep(2)
                else:
                    print(f"{blue_color}No se actualizó el curso")
                    time.sleep(2)
                break
        
        if not curso_encontrado:
            print(f"{blue_color}El curso no existe o no está activo")
            time.sleep(2)

    def delete(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{green_color}Eliminar Curso")
        linea(80, green_color)
        
        id_curso_str = input(f"{blue_color}Ingrese el ID del curso a eliminar: {green_color}")
        id_curso = Valida.solo_numeros(
            entrada=id_curso_str,
            mensaje_error="El ID debe ser un número válido",
            col=10,  # Ajusta según tu diseño
            fil=10   # Ajusta según tu diseño
        )
        
        if id_curso is None:
            print(f"{blue_color}ID inválido. Regresando al menú principal.")
            time.sleep(2)
            return
        
        cursos = self.json_file.read()  
        linea(80, green_color)
        curso_encontrado = False
        for curso in cursos:
            if curso["id"] == id_curso and curso["active"]:
                curso_encontrado = True
                print(f"{blue_color}Curso encontrado: {green_color}{curso['nombre']}")
                confirmacion = input(f"{blue_color}¿Está seguro de eliminar el curso? s/n: {green_color}")
                if confirmacion.lower() == 's':
                    curso["active"] = False
                    self.json_file.save(cursos)
                    print(f"{green_color}Curso eliminado correctamente")
                    time.sleep(2)
                else:
                    print(f"{blue_color}No se eliminó el curso")
                    time.sleep(2)
                break
        
        if not curso_encontrado:
            print(f"{blue_color}El curso no existe o ya está inactivo")
            time.sleep(2)
            
    def consult(self):
        BorrarPantalla()
        linea(80, green_color)
        gotoxy(32, 2); print(f"{green_color}Mostrar Cursos")
        linea(80, green_color)
        
        cursos = self.json_file.read()
        
        menu = Menu("Seleccione una opción", ["Mostrar todos los cursos", "Buscar curso por ID", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
        opc = menu.menu()
        
        if opc == '1':
            BorrarPantalla()
            linea(80, green_color)
            gotoxy(32, 2); print(f"{green_color}Todos los Cursos")
            linea(80, green_color)
            
            if cursos:
                cursos_encontrados = False
                for curso in cursos:
                    if curso['active']:
                        print(f"{blue_color}ID: {green_color}{curso['id']}\n{blue_color}Nombre: {green_color}{curso['nombre']}\n{blue_color}Fecha de Creación: {green_color}{curso['fecha_creacion']}\n")
                        cursos_encontrados = True
                if not cursos_encontrados:
                    print(f"{green_color}No hay cursos registrados.")
            else:
                print(f"{green_color}No hay cursos registrados.")
            time.sleep(3)
        
        elif opc == '2':
            id_curso_str = input(f"{blue_color}Ingrese el ID del curso a buscar: {green_color}")
            id_curso = Valida.solo_numeros(
                entrada=id_curso_str,
                mensaje_error="El ID debe ser un número válido",
                col=10,  # Ajusta según tu diseño
                fil=10   # Ajusta según tu diseño
            )
            
            if id_curso is None:
                print(f"{blue_color}ID inválido. Regresando al menú principal.")
                time.sleep(2)
                return
            
            cursos_encontrados = False
            for curso in cursos:
                if curso['id'] == id_curso and curso['active']:
                    print(f"{blue_color}Curso encontrado: {green_color}{curso['nombre']}\n{blue_color}Fecha de Creación: {green_color}{curso['fecha_creacion']}")
                    cursos_encontrados = True
                    break
            if not cursos_encontrados:
                print(f"{blue_color}No se encontró un curso con ID {id_curso}.")
            time.sleep(3)
        
        elif opc == '3':
            print(f"{blue_color}Regresando al menú principal.")
            time.sleep(2)
