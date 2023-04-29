import cv2
import numpy as np
import math
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)  # 0 is id to use webcam 
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300
counter = 0

folder = "Data/No"
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']  # axis


        # Create Image matrix using numpy
        imgWhite = np.ones((imgSize, imgSize, 3),
                           np.uint8) * 255  # here we consider image code of 8bitn (color image range 255)

        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        imgCropShape = imgCrop.shape

        # calculations for arrange webcam video on whiteimg perfectly

        aspectRatio = h / w  # h=height w=width
        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)

        imgResize = cv2.resize(imgCrop, (wCal, imgSize))
        imgResizeShape = imgResize.shape
        # To get image in center
        wGap = math.ceil((imgSize - wCal) / 2)  # imgsize = 300 wcal(Calculated width) divide by 2
        imgWhite[:, wGap:wCal + wGap] = imgResize

   # else:
      #  k = imgSize / w
       # hCal = math.ceil(k * h)

       # imgResize = cv2.resize(imgCrop, (imgSize, hCal))
        imgResizeShape = imgResize.shape
        # To get image in center
      #  hGap = math.ceil((imgSize - hCal) / 2)  # imgsize = 300 wcal(Calculated width) divide by 2
       # imgWhite[hGap:hCal + hGap, :] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)

