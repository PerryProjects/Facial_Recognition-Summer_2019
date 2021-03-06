'''
Program to detect faces from image feed in real time.
You must install: 
1.  python openCV library 
    1A. open CMD and type: pip install opencv-python
2.  haarcascade_eye.xml
    2A. download link: 
        https://github.com/opencv/opencv/tree/master/data/haarcascades
3.  haarcascade_frontalface_default.xml
    3A. down link:
        https://github.com/opencv/opencv/tree/master/data/haarcascades
4.  place both .xml files in the same directory as .py 
    or change directory paths in code  

The .xml files store pre-trained openCV classifiers
Unique data to identify specific features of an object
A cascade is trained from positive and negative objects
These cascades are pre-trained with 
Images containing human faces faces and eyes
'''
# import python OpenCV   
import cv2  
 
# load openCV trained XML classifiers 
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

# Trained XML file for detecting eyes 
cascade_eye = cv2.CascadeClassifier('haarcascade_eye.xml')  
  
# camera_capture frames from a camera
# cv2.Videocamera_capture uses your webcam feed by default
camera_cap = cv2.VideoCapture(0) 
 
# run if camera_cap has been initialized. 
while True:  
  
    # reads the individual frames from camera_cam 
    ret, img = camera_cap.read()  
  
    # convert frames to gray scale, faster detection 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
    # Detect faces in the image 
    cam_faces = cascade_face.detectMultiScale(gray, 1.4, 4) 
  
    for (x,y,w,h) in cam_faces: 
        # Draw a rectangle in the face  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
  
        # Detects eyes in the image 
        eyes = cascade_eye.detectMultiScale(roi_gray, 1.3, 5)  
  
        #Draw a rectangle in the eyes 
        for (ax,ay,aw,ah) in eyes: 
            cv2.rectangle(roi_color,(ax,ay),(ax+aw,ay+ah),(0,255,255),2) 
  
    # Display an image in a window 
    cv2.imshow('facial recognition from live feed',img) 
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
# Close the window 
camera_cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  
