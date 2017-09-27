from docx import Document


def delete_paragraph(paragraph):
	p = paragraph._element
	p.getparent().remove(p)
	p._p = p._element = None


def crear_guia(input_doc_name, output_doc_name, sep, questions):
	#cargar documento
	document = Document(input_doc_name)
	paragraphs = document.paragraphs

	#encontar separadores y meter sus indices en seps
	seps = [0]
	# count = 0
	for i in range(len(paragraphs)):
		if paragraphs[i].text == sep:
			# count += 1
			seps.append(i)
			paragraphs[i].text = ''
	# print(seps)
	# print(count)

	#eliminar preguntar no requeridas
	inicio = 0
	fin = 0
	for q in questions:
		fin = seps[q-1]
		# print(inicio, fin)
		#inicio dejar preguntas juntas!
		if inicio == fin:
			for x in range(fin + 1, seps[q] - 1):
				if paragraphs[x].text != '':
					paragraphs[x].paragraph_format.keep_with_next = True
		#fin dejar preguntas juntas
		for j in range(inicio, fin):
			delete_paragraph(paragraphs[j])
		inicio = seps[q]
	for i in range(inicio, len(paragraphs)):
		delete_paragraph(paragraphs[i])


	#crear nueva guia
	document.save(output_doc_name)


#crear_guia('invierno.docx', 'output1.docx', '*', [1, 2, 3, 4, 5, 6, 9, 10, 15, 18, 20])