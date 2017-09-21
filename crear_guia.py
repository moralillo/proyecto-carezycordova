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
	for i in range(len(paragraphs)):
		if paragraphs[i].text == sep:
			seps.append(i)
			paragraphs[i].text = ''
	print(seps)

	#eliminar preguntar no requeridas
	inicio = 0
	fin = 0
	for q in questions:
		fin = seps[q-1]
		print(inicio, fin)
		for j in range(inicio, fin):
			delete_paragraph(paragraphs[j])
		inicio = seps[q]
	for i in range(inicio, len(paragraphs)):
		delete_paragraph(paragraphs[i])

	#crear nueva guia
	document.save(output_doc_name)


crear_guia('invierno.docx', 'output1.docx', '*', [1, 5, 7, 15, 18])