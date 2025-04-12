# Install necessary libraries
# pip install opencv-python librosa numpy tensorflow keras

import cv2
import librosa
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load pretrained emotion recognition model (for facial expressions)
emotion_model = load_model('emotion_model.h5')  # Replace with the actual path to your model
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Function to analyze facial expressions
def analyze_facial_expression(image_path):
    # Load image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray_image[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        roi_gray = roi_gray.astype('float') / 255.0
        roi_gray = img_to_array(roi_gray)
        roi_gray = np.expand_dims(roi_gray, axis=0)

        # Predict emotion
        predictions = emotion_model.predict(roi_gray)[0]
        emotion_index = np.argmax(predictions)
        emotion = emotion_labels[emotion_index]

        print(f"Detected Emotion: {emotion}")
        return emotion

    return "No face detected"

# Function to analyze audio (voice tone)
def analyze_voice_tone(audio_path):
    # Load audio file
    audio, sample_rate = librosa.load(audio_path, sr=22050)

    # Extract features
    mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
    mfcc_mean = np.mean(mfcc.T, axis=0)

    # Dummy model for demonstration (replace with your trained model)
    # Here, we simply classify based on arbitrary thresholds for demonstration purposes
    emotion = "Neutral"
    if mfcc_mean[0] > 50:
        emotion = "Happy"
    elif mfcc_mean[0] < -50:
        emotion = "Sad"

    print(f"Detected Voice Emotion: {emotion}")
    return emotion

# Example usage
if __name__ == "__main__":
    # Test facial expression analysis
    print("Facial Expression Analysis:")
    facial_emotion = analyze_facial_expression('test_image.jpg')  # Replace with your test image path
    print(f"Facial Emotion: {facial_emotion}")

    # Test voice tone analysis
    print("\nVoice Tone Analysis:")
    voice_emotion = analyze_voice_tone('test_audio.wav')  # Replace with your test audio path
    print(f"Voice Emotion: {voice_emotion}")
    