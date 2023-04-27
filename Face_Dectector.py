# Import cv2, this is after installing Open CV

import cv2 

# load some pre-trained data on frontal faces
trained_faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# choose an image to detect the face
# img = cv2.imread('kelvin hart.jpg')
# img = cv2.imread('plenty faces.png')

# Capturing video from webcam
webcam = cv2.VideoCapture(0)

while True:
    real_face_detected, frame = webcam.read()

    # convert image to greyscale, open cv's algorithm can only work well with black and white
    greyscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    face_coordinates = trained_faces.detectMultiScale(greyscaled_image)

    # Draw rectangles around faces
    # x, y,w, h are axis of the face cordinates
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)


    cv2.imshow('Face Detection', frame)
    key = cv2.waitKey(1)

    # stop if key Q or q is pressed, the value of key here is Q in ASCII (check it out)
    if key==81 or key==113:
        break

# Stop the VideoCapture object when done
webcam.release()
    

print('code completed')











'''
# convert image to greyscale, open cv's algorithm can only work well with black and white
greyscaled_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# detect faces
face_coordinates = trained_faces.detectMultiScale(greyscaled_image)

# Draw rectangles around faces
# x, y,w, h are axis of the face cordinates
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)


# code to show image and code to make the image wait after showing
cv2.imshow('CLever Programmer Face Detector', img)
cv2.waitKey()


print("Code Completed")


''' 