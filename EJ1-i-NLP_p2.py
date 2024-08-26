from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

archivo_imagen = 'img_pdf\pagina0.png'

imagen = Image.open(archivo_imagen)

texto = pytesseract.image_to_string(imagen)

print(texto)