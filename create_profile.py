import cv2
import os

# Directly target the cv2.cv2 core module wrapper to bypass the namespace bug
try:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
except AttributeError:
    # Fallback for version 5.0+ module layout differences
    face_cascade = cv2.cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

print("[INFO] Look directly at the camera. Press 's' to save your face profile or 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # Handle both tuple and numpy array return formats safely
    has_faces = False
    if isinstance(faces, tuple):
        if len(faces) > 0: has_faces = True
    elif isinstance(faces, np.ndarray):
        if faces.size > 0: has_faces = True

    if has_faces:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    cv2.imshow("Register Face - JARVIS Security", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s') and has_faces:
        # Crop and save the first detected face region safely
        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            cv2.imwrite("my_face.jpg", cv2.resize(face_img, (200, 200)))
            print("[SUCCESS] Face profile saved as 'my_face.jpg'!")
            break
        break
    elif key == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
