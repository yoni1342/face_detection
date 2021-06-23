
# import cv2
# from random import randrange

# trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
# #read the image frrom the directory
# img = cv2.imread('ba.jpg')

# #must converted to the gray scale 
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #Detect_face
# face_cordinate = trained_face_data.detectMultiScale(grayscaled_img)

# print(face_cordinate)
# for (x, y, w, h)in face_cordinate:
#     cv2.rectangle(img, (x, y), (w+x, y+h), (randrange(256), randrange(256), randrange(256)), 2)

# #display the image 
# cv2.imshow('img', img)
# #wait showing the image unil some one press the key
# cv2.waitKey()


# import cv2
# from random import randrange
# ternd_face_detection = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
# video = cv2.VideoCapture(0)

# while True:
#     su, img = video.read()
#     gray_sacled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#     face_cordinate = ternd_face_detection.detectMultiScale(gray_sacled_img)
#     print(face_cordinate)
#     for(x, y, w, h)in face_cordinate:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(256),randrange(256),randrange(256)), 2)
#     cv2.imshow("web", img)
#     if cv2.waitKey(1) & 0xff == ord('q'):
#         break



import cv2
teraind_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

while True:
    su, img = video.read()
    gray_sacled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cordinate = teraind_face_data.detectMultiScale(gray_sacled_img)
    print(face_cordinate)
    for (x, y, w, h) in face_cordinate:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("web", img)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break