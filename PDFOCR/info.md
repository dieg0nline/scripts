# Requisitos previos

1. **Instalar las bibliotecas necesarias**:
   - Asegúrate de tener instaladas las siguientes bibliotecas:

   ```bash
   pip install pytesseract pdf2image Pillow
   ```

2. **Instalar Tesseract**:
   - Si aún no lo tienes instalado, sigue las instrucciones para tu sistema operativo:
     - **Windows**: Descarga [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
     - **Linux**: Usa el gestor de paquetes de tu distribución, por ejemplo:

       ```bash
       sudo apt install tesseract-ocr
       ```

     - **macOS**: Usa Homebrew:

       ```bash
       brew install tesseract
       ```

## Script Python para OCR de PDF

Una vez que hayas instalado las dependencias, puedes usar este script para convertir el PDF en texto usando OCR:

```python
from pdf2image import convert_from_path
import pytesseract
import os

# Ruta del archivo PDF
pdf_path = "ruta_a_tu_archivo.pdf"

# Convierte el PDF en imágenes
images = convert_from_path(pdf_path)

# Opcional: Define la ruta de instalación de Tesseract (solo en Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Variable para almacenar el texto extraído
ocr_text = ""

# Realiza OCR en cada imagen
for i, image in enumerate(images):
    # Convierte la imagen a texto
    text = pytesseract.image_to_string(image)
    ocr_text += f"--- Página {i+1} ---\n\n{text}\n\n"

# Guarda el texto en un archivo
with open("texto_extraido.md", "w", encoding="utf-8") as f:
    f.write(ocr_text)

print("OCR completado y texto guardado en 'texto_extraido.md'.")
```

## Explicación de los pasos

1. **Convertir el PDF en imágenes**: Usamos `pdf2image` para convertir cada página del PDF en una imagen.
2. **Realizar OCR en cada imagen**: Usamos `pytesseract` para extraer el texto de cada una.
3. **Guardar el resultado**: Todo el texto extraído se guarda en un archivo `texto_extraido.md`.

## Personalización

- Si quieres mejorar la precisión del OCR, puedes cambiar el idioma en `pytesseract`:
  
  ```python
  text = pytesseract.image_to_string(image, lang='spa')  # Para español
  ```

- Puedes ajustar la resolución de las imágenes si el PDF tiene texto pequeño o difícil de leer:
  
  ```python
  images = convert_from_path(pdf_path, dpi=300)
  ```

Esto debería darte una extracción precisa del texto de tu PDF. Si tienes alguna duda mientras lo ejecutas, ¡avísame!