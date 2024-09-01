import cv2
import pytesseract


def detect_chars(img):
    boxes = pytesseract.image_to_boxes(img)
    hImg = img.shape[0]
    wImg = img.shape[1]
    text_offset = 40

    for b in boxes.splitlines():
        b=b.split(' ')
        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
        cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
        cv2.waitKey(0)
        cv2.putText(img,b[0],(x,hImg-y-text_offset),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),2)

    cv2.imshow('Result',img)
    cv2.waitKeboxes(0)

def detect_words(img):
    boxes = pytesseract.image_to_data(img)
    hImg = img.shape[0]
    wImg = img.shape[1]
    text_offset = 5

    for x,b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()

            if len(b)>=12:
                print(b[11])
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),1)
                cv2.putText(img, b[11], (x, y-text_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)
                cv2.waitKey(0)


                cv2.imshow('Result', img)
                cv2.rectangle(img,(x,y),(w+x,h+y),(255,255,255),1)
                cv2.putText(img, b[11], (x, y-text_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


def visualize_image(img):
    white_threshold = 250
    for line in img:
        for pixel in line:
            if pixel>=white_threshold:
                print('0',end='')
            else:
                print('1',end='')
        print('')

loading language \'eng\' Tesseract couldn\'t load any languages! Could not initialize tesseract.'