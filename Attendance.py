import numpy as np
import cv2
import face_recognition
from datetime import datetime
import os
#------------------------------------------------------------------------------------------------------------------------
blue = (179, 164, 138)
dark_blue = (81, 57, 33)
bright_blue = (231, 255, 214)
pink = (106, 129, 207)
frameWidth, frameHeight = 480, 640
#------------------------------------------------------------------------------------------------------------------------
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def encoding(images):
    encodedImgs = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodedImg = face_recognition.face_encodings(img)[0]
        encodedImgs.append(encodedImg)
    return encodedImgs

def markAttendance(name):
    with open('Resources/Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

# Read images
images = []
className = []
path = 'Resources/Attendance'
list = os.listdir(path)
for img in list:
    curImg = cv2.imread(os.path.join(path, img))
    images.append(curImg)
    className.append(os.path.splitext(img)[0])
print('Attendance list: ', list)
print('Class Names: ', className)

# Encoding
encodedImgs = encoding(images)
print('Encoding completed!')

# Face comparing using webcam
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
while True:
    success, img = cap.read()
    # img = captureScreen()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    currentFace = face_recognition.face_locations(imgS)
    encodedCurrentFace = face_recognition.face_encodings(imgS, currentFace)

    for encodedFace, faceLocation in zip(encodedCurrentFace, currentFace):
        matches = face_recognition.compare_faces(encodedImgs, encodedFace)
        faceDis = face_recognition.face_distance(encodedImgs, encodedFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = className[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), dark_blue, 2)
            cv2.rectangle(img, (x1, y2 - 25), (x2, y2), dark_blue, cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.6, bright_blue, 2)
            markAttendance(name)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        name = name + '.jpg'
        img
        cv2.imwrite(os.path.join('Resources/Realtime Image', name), img)
        cv2.rectangle(img, (0,452), (640,480),
                      dark_blue, cv2.FILLED)
        cv2.putText(img=img, text='Image Saved', org=(260,470),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, color=bright_blue, thickness=1)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
