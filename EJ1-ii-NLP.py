from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

archivo_imagen = r'Archivos\foto.jpg'

imagen = Image.open(archivo_imagen)

texto = pytesseract.image_to_string(imagen)

print(texto)