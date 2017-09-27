import os
#from crear_guia import crear_guia


def generar_guia(guia, resultado, dir_a_alumno):
    output = resultado.strip('xlsx') + 'docx'
    dir_guia = os.getcwd() + '/guias' + 'ensayo' + str(guia) + '.docx'
    sep = '8==D'
    crear_guia(dir_guia, output, sep, resultado, dir_a_alumno)


guia = input('Ingrese guia que quiere generar: ')

alumnos = os.listdir(os.getcwd() + '/alumnos')

for alumno in alumnos:
    if len(alumno) > 10:
        dir_a_alumno = os.getcwd() + '/alumnos/' + alumno
        lista_resultados = os.listdir(dir_a_alumno)
        for resultado in lista_resultados:
            print(resultado, type(resultado))
            if 'xlsx' in resultado and str(guia) in resultado:
                generar_guia(guia, resultado, dir_a_alumno)