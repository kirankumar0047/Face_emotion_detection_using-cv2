😊 Real-Time Face Emotion Detection System:

![developer](https://img.shields.io/badge/Developed%20By%20%3A-Sumit%20Kumar-red)
---

This project is a real-time face emotion detection system built using OpenCV, DeepFace, and other deep learning libraries. It detects facial expressions such as **Happy**, **Sad**, **Neutral**, **Angry**, etc., with a green bounding box and displays the emotion name along with prediction accuracy. It also plays an emotion-based sound and detects fake/deepfake faces with an error message.

Features
- ✅ Real-time face detection using webcam
- 😊 Emotion classification (Happy, Sad, Neutral, etc.)
- 🟩 Green square around each detected face
- 🔊 Plays emotion-based audio
- 🧠 Detects and blocks fake/deepfake faces
- 📊 Displays emotion label and confidence (accuracy)
- 🚫 Shows an error message if a fake face is detected

💡 Innovation Over Existing Projects

Most face emotion projects only:
- Detect a single face
- Show basic emotion labels
- Do not handle fake face detection
- Do not play audio

This project includes:
- Multi-face detection
- Real-time feedback with emotion sounds
- Deepfake/fake face rejection
- Green bounding boxes with live emotion + accuracy label

🧠 Libraries Used

| Library     | Purpose                             |
|-------------|-------------------------------------|
| OpenCV      | Video stream and face detection     |
| DeepFace    | Emotion recognition                 |
| RetinaFace  | Accurate face detection             |
| Playsound   | Play emotion-related sounds         |
| TensorFlow  | Backend for deep learning models    |
| Keras       | Neural network model loading        |
| tf-keras    | Keras compatibility for newer TF    |

🛠️ Installation

Set up virtual environment (optional but recommended):
python -m venv .venv
source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Run the Application:
 python app.py
