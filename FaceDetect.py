import cv2
# import numpy as np

image = cv2.imread('images.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
                   
   )
   
print("Found {0} Faces!".format(len(faces)))
while True:

    for (x, y, w, h) in faces:

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow('img',image)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
         break;
status = cv2.imwrite('faces_detected.jpg', image)
print("[INFO] Image faces_detected.jpg written to filesystem: ", status)

print(image)







# face_cascade  = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade =  cv2.CascadeClassifier('haarcascade_eye.xml')

# cap = cv2.imread('images.jpg',0)

# while True :
#     ret ,img = cap.read()
#     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray,1.3,5)
#     for (x,y,w,h) in faces :
#         c2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#         roi_gray = gray[y:y+h,x:x+w]
#         roi_color =  img[y:y+h,x:x+w]

#         eyes = eye_cascade.detectMultiScale(roi_gray)
#         for(ex,ey,eh,ew) in eyes :
#             cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # cv2.imshow('img0',img)
    # k = cv2.waitKey(30) & 0xff
    # if k == 27:
    #     break;

image.release()
cv2.destroyAllWindows()                

