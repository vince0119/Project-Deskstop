import cv2 as cv
import imutils
import keyboard
import numpy as np
import pytesseract 




def plate_Detection(img):
    max_size =  img.shape
    min_size = (img.shape[0] *30/100, img.shape[1] *30/100,img.shape[2] *30/100)
    pytesseract.pytesseract.tesseract_cmd ="C:/Program Files/Tesseract-OCR/tesseract.exe"
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11,17,17)
    edged = cv.Canny(gray, 30, 200)

    cnts = cv.findContours(edged.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv.contourArea, reverse=True)
    # cv.imshow("gray",gray)
    # cv.imshow("edge",edged)
    screenCnt = None

    #loop over our contours
    for c in cnts:
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.05 * peri, True)
        
        if len(approx) == 4 and (max_size[0]*max_size[1]*max_size[2]) > cv.contourArea(c) > (min_size[0]*min_size[1]*min_size[2]):
            screenCnt = approx
            cv.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
            mask = np.zeros(gray.shape, np.uint8)
            new_image = cv.drawContours(mask, [screenCnt], 0, 255, -1, )
            new_image = cv.bitwise_and(img, img, mask=mask)
            
            (x, y) = np.where(mask == 255)
            (topx, topy) = (np.min(x), np.min(y))
            (bottomx, bottomy) = (np.max(x), np.max(y))
            Cropped = gray[topx:bottomx +10, topy:bottomy + 10]
            _,img_otsu = cv.threshold(Cropped,127,255, cv.THRESH_BINARY+cv.THRESH_OTSU)
            # cv.imshow('Liscense plate', img_otsu)
            result = pytesseract.pytesseract.image_to_string(img_otsu)
            return result
            

def OpenCamera(img):

    string = plate_Detection(img)
    if (string == None):
        string = ""
    
    filter = ""
    for i in string:
        if (i.isnumeric() or i.isalpha()):
            filter+=i
    return filter
    
       

