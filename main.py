import cv2
import pytesseract
import functions
from matplotlib import pyplot as plt

functions.tesseract_setup()

capture = functions.capture_setup()

while capture.isOpened():
    ret, frame = capture.read()

    cv2.imshow('webcam capture',frame)
    plt.show()
    #functions.detect_words(frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

