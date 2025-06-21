import cv2
from deepface import DeepFace
from playsound import playsound
import numpy as np
import random

# Dummy liveness function (replace with real model)
def is_real_face(face_img):
    # TODO: Integrate a real anti-spoofing model
    return random.choice([True, True, True, False])  # Simulate mostly real faces

# Emotion to sound mapping
emotion_sounds = {
    'happy': 'sounds/happy.mp3',
    'sad': 'sounds/sad.mp3',
    'neutral': 'sounds/neutral.mp3',
    'angry': 'sounds/angry.mp3',
    'surprise': 'sounds/surprise.mp3',
    'fear': 'sounds/fear.mp3',
    'disgust': 'sounds/disgust.mp3'
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

    for face in result:
        x, y, w, h = face['region']['x'], face['region']['y'], face['region']['w'], face['region']['h']
        emotion = face['dominant_emotion']
        acc = face['emotion'][emotion]

        face_img = frame[y:y+h, x:x+w]
        real = is_real_face(face_img)

        if not real:
            label = "Fake Face Detected"
            color = (0, 0, 255)  # Red
        else:
            label = f"{emotion.capitalize()} ({round(acc, 2)}%)"
            color = (0, 255, 0)  # Green
            if emotion in emotion_sounds:
                try:
                    playsound(emotion_sounds[emotion], block=False)
                except:
                    pass  # Avoid blocking or crash if file not found

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow('Face Emotion Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()