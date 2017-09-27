import xlrd


def encontrar_malas(archivo):
    workbook = xlrd.open_workbook(archivo)
    sheet = workbook.sheet_by_index(0)

    lista_preguntas = []
    lista_respuestas = []
    lista_preguntas_ordenadas = []
    lista_respuestas_ordenadas = []

    if sheet.nrows > 70:
        tipo = 1
    else:
        tipo = 2

    if tipo == 1:
        for rowx in range(sheet.nrows):
            cols = sheet.row_values(rowx)
            if cols[8] == 'Mala' or cols[8] == 'Omitida':
                lista_preguntas_ordenadas.append(int(cols[6]))
                lista_respuestas_ordenadas.append(cols[9])

    elif tipo == 2:
        for rowx in range(sheet.nrows):
            cols = sheet.row_values(rowx)
            if cols[6] == 'Mala' or cols[6] == 'Omitida':
                lista_preguntas.append(int(cols[1]))
                lista_respuestas.append(cols[8])
            if cols[18] == 'Mala' or cols[18] == 'Omitida':
                lista_preguntas.append(int(cols[14]))
                lista_respuestas.append(cols[20])

        for i in range(len(lista_preguntas)):
            minimo = min(lista_preguntas)
            lista_preguntas_ordenadas.append(minimo)
            respuesta_correspondiente = lista_respuestas[lista_preguntas.index(minimo)]
            lista_respuestas_ordenadas.append(respuesta_correspondiente)

            lista_preguntas.remove(minimo)
            lista_respuestas.remove(respuesta_correspondiente)



    return lista_preguntas_ordenadas, lista_respuestas_ordenadas






