import numpy as np
import cv2
import face_recognition

#------------------------------------------------------------------------------------------------------------------------
blue = (179, 164, 138)
dark_blue = (81, 57, 33)
square_size = (640, 640)
rec_size_h = (480, 640)
rec_size_v = (860, 640)
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

def resize(img):
    w = img.shape[0]
    h = img.shape[1]
    if w/h > 0.8 and w/h < 1.2:
        img = cv2.resize(img, square_size)
    elif w/h < 0.8:
        img = cv2.resize(img, rec_size_v)
    else:
        img = cv2.resize(img, rec_size_h)
    return  img

img =  face_recognition.load_image_file('Resources/Basic/brand1.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faceLocation = face_recognition.face_locations(img)[0]
faceEncode = face_recognition.face_encodings(img)[0]

imgTest = face_recognition.load_image_file('Resources/Basic/tyrion2.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
faceLocationTest = face_recognition.face_locations(imgTest)[0]
faceEncodeTest = face_recognition.face_encodings(imgTest)[0]
print('Encoded all images')

result = face_recognition.compare_faces([faceEncode], faceEncodeTest)
distance = face_recognition.face_distance([faceEncode], faceEncodeTest)

# Display
print('faceLocation', faceLocation)
print('faceEncode', faceEncode.shape)
print('Are they one: ', result)
print('Distance: ', distance)

cv2.rectangle(img, (faceLocation[3], faceLocation[0]), (faceLocation[1],faceLocation[2]),
              color=blue, thickness=2)
cv2.rectangle(imgTest, (faceLocationTest[3],faceLocationTest[0]), (faceLocationTest[1],faceLocationTest[2]),
              color=blue, thickness=2)
cv2.putText(imgTest,f'{result} {round(distance[0], 2)}',(faceLocationTest[3], faceLocationTest[0]-10),
            fontFace=cv2.FONT_ITALIC, fontScale=0.5, color=dark_blue, thickness= 2)
img = resize(img)
imgTest = resize(imgTest)
imgStack = stackImages(1, ([img, imgTest]))
cv2.imshow('Comparison', imgStack)
cv2.waitKey(50000)