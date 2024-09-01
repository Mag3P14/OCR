import cv2
import pytesseract
import functions

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('qrcode.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#functions.detect_chars(img)

functions.detect_words(img)