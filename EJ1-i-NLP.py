from pdf2image import convert_from_path
import PyPDF2

pop_path = r'C:\Users\Ignacio González\Desktop\unr\2A - 2C\NLP\poppler-24.07.0\Library\bin'

imagenes = convert_from_path('EJ1.pdf', poppler_path=pop_path)

for i, imagen in enumerate(imagenes):
    imagen.save('pagina{}.png'.format(i), 'PNG')

