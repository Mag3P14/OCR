import cv2
import pytesseract
import functions
from matplotlib import pyplot as plt

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
FPS = 60
cap.set(cv2.CAP_PROP_FPS, FPS)
#width = 1920
#height = 1080
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#img = cv2.imread('qrcode.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

while cap.isOpened():
    ret, frame = cap.read()

    #cv2.imshow('webcam',frame)
    #plt.show()
    functions.detect_words(frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

