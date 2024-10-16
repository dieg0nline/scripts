# Retry the OCR process again using PDF to images and Tesseract for OCR extraction
from pdf2image import convert_from_path
import pytesseract

# Convert PDF to images
pdf_path = '/mnt/data/DEUC.pdf'
images = convert_from_path(pdf_path)

# Perform OCR on the extracted images
ocr_text = ""
for image in images:
    text = pytesseract.image_to_string(image)
    ocr_text += text + "\n\n"

# Show the first 2000 characters of the OCR result as a preview
ocr_text[:2000]
