from utilss import reset_color, green_color, blue_color
from utilss import BorrarPantalla, gotoxy
from CrudAsignatura import CrudAsignatura
from CrudEstudiante import CrudEstudiante
from CrudNivel import CrudNivel
from CrudPeriodo import CrudPeriodo
from CrudProfesor import CrudProfesor
from CrudNota import CrudNota
from Componets import Menu
from CrudCurso import CrudCurso
from CrudMatricula import CrudMatricula  # Importa el CRUD para Matrícula

import time

opc = ''
while opc != '9':  # Cambiado para que coincida con la nueva opción de salida
    BorrarPantalla()
    menu_main = Menu("Menu Principal", ["Gestion de Periodos", "Gestion de Nivel", "Gestion de Asignaturas", "Gestion de Profesores", "Gestion de Estudiantes", "Gestion de Notas", "Gestion de Cursos", "Gestion de Matriculas", "Salir"], color=green_color, color_numeros=blue_color)
    opc = menu_main.menu()
    
    if opc == '1':
        opc1 = ''
        while opc1 != '5':
            BorrarPantalla()
            menu_periodo = Menu("Menu Periodo", ["Registrar Periodo", "Eliminar Periodo", "Actualizar Periodo", "Mostrar Periodos", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc1 = menu_periodo.menu()
            crud = CrudPeriodo()
            if opc1 == '1':
                crud.create()
            elif opc1 == '2':
                crud.delete()
            elif opc1 == '3':
                crud.update()
            elif opc1 == '4':
                crud.consult()
            elif opc1 == '5':
                print("Regresando al menú principal...")
                time.sleep(2)

    elif opc == '2':
        opc2 = ''
        while opc2 != '5':
            BorrarPantalla()
            menu_nivel = Menu("Menu Nivel", ["Registrar Nivel", "Eliminar Nivel", "Actualizar Nivel", "Mostrar Niveles", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc2 = menu_nivel.menu()
            crud = CrudNivel()
            if opc2 == '1':
                crud.create()
            elif opc2 == '2':
                crud.delete()
            elif opc2 == '3':
                crud.update()
            elif opc2 == '4':
                crud.consult()
            elif opc2 == '5':
                print("Regresando al menú principal...")
                time.sleep(2)

    elif opc == '3':
        opc3 = ''
        while opc3 != '5':
            BorrarPantalla()
            menu_asignatura = Menu("Menu Asignatura", ["Registrar Asignatura", "Eliminar Asignatura", "Actualizar Asignatura", "Mostrar Asignaturas", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc3 = menu_asignatura.menu()
            crud = CrudAsignatura()
            if opc3 == '1':
                crud.create()
            elif opc3 == '2':
                crud.delete()
            elif opc3 == '3':
                crud.update()
            elif opc3 == '4':
                crud.consult()
            elif opc3 == '5':
                print("Regresando al menú principal...")
                time.sleep(2)

    elif opc == '4':
        opc4 = ''
        while opc4 != '5':
            BorrarPantalla()
            menu_profesor = Menu("Menu Profesor", ["Registrar Profesor", "Eliminar Profesor", "Actualizar Profesor", "Mostrar Profesores", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc4 = menu_profesor.menu()
            crud = CrudProfesor()
            if opc4 == '1':
                crud.create()
            elif opc4 == '2':
                crud.delete()
            elif opc4 == '3':
                crud.update()
            elif opc4 == '4':
                crud.consult()
            elif opc4 == '5':
                print("Regresando al menú principal...")
                time.sleep(2)

    elif opc == '5':
        opc5 = ''
        while opc5 != '5':
            BorrarPantalla()
            menu_estudiante = Menu("Menu Estudiante", ["Registrar Estudiante", "Eliminar Estudiante", "Actualizar Estudiante", "Consultar Estudiantes", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc5 = menu_estudiante.menu()
            crud = CrudEstudiante()
            if opc5 == '1':
                crud.create()
            elif opc5 == '2':
                crud.delete()
            elif opc5 == '3':
                crud.update()
            elif opc5 == '4':
                crud.consult()
            elif opc5 == '5':
                print("Regresando al menú principal...")
                time.sleep(2)

    elif opc == '6':
        opc6 = ''
        while opc6 != '5':
            BorrarPantalla()
            menu_nota = Menu("Menu Nota", ["Registrar Nota", "Eliminar Nota", "Actualizar Nota", "Mostrar Notas", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc6 = menu_nota.menu()
            crud = CrudNota()
            if opc6 == '1':
                crud.create()
            elif opc6 == '2':
                crud.delete()
            elif opc6 == '3':
                crud.update()
            elif opc6 == '4':
                crud.consult()
            elif opc6 == '5':
                print("Regresando al menú principal...")
                time.sleep(2)

    elif opc == '7':
        opc7 = ''
        while opc7 != '5':
            BorrarPantalla()
            menu_curso = Menu("Menu Curso", ["Registrar Curso", "Eliminar Curso", "Actualizar Curso", "Consultar Cursos", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc7 = menu_curso.menu()
            crud = CrudCurso()
            if opc7 == '1':
                crud.create()
            elif opc7 == '2':
                crud.delete()
            elif opc7 == '3':
                crud.update()
            elif opc7 == '4':
                crud.consult()
            elif opc7 == '5':
                print("Regresando al menú principal...")
                time.sleep(2)

    elif opc == '8':
        opc8 = ''
        while opc8 != '5':
            BorrarPantalla()
            menu_matricula = Menu("Menu Matricula", ["Registrar Matricula", "Eliminar Matricula", "Actualizar Matricula", "Mostrar Matriculas", "Volver al menú principal"], color=green_color, color_numeros=blue_color)
            opc8 = menu_matricula.menu()
            crud = CrudMatricula()  # Instancia del CRUD para Matrícula
            if opc8 == '1':
                crud.create()
            elif opc8 == '2':
                crud.delete()
            elif opc8 == '3':
                crud.update()
            elif opc8 == '4':
                crud.consult()
            elif opc8 == '5':
                print("Regresando al menú principal...")
                time.sleep(2)

    elif opc == '9':
        break

    print("Regresando al menú principal...")
    time.sleep(2)

BorrarPantalla()
input("Gracias por usar el sistema, presione una tecla para salir...")
BorrarPantalla()
