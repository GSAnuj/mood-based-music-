# MOOD-BASED MUSIC PLAYER
import cv2
from deepface import DeepFace
import pygame
import time
import os

# Initialize music library
mood_music = {
    "happy": "project/music/sunny.mp3",
    "sad": "project/music/sad.mp3",
    "angry": "project/music/actionable.mp3",
    "surprise": "project/music/surprise.mp3",
    "neutral": "project/music/floatinggarden.mp3",
    "fear": "project/music/silentsuspicions.mp3",
    "disgust": "project/music/disgust.mp3"
}

# Setup pygame mixer
pygame.mixer.init()

def play_music(emotion):
    music_file = mood_music.get(emotion)
    if music_file and os.path.exists(music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  # -1 means loop
        print(f"🎵 Now playing music for: {emotion}")
    else:
        print(f"⚠️ Music file not found for emotion: {emotion}")

def stop_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

def real_time_mood_music():
    cap = cv2.VideoCapture(0)
    last_emotion = None
    last_detection_time = time.time()

    print("📷 Starting real-time mood detection. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Show live webcam feed
        cv2.imshow("Mood Detection | Press 'q' to quit", frame)

        # Limit detection frequency (e.g., every 5 seconds)
        if time.time() - last_detection_time >= 5:
            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                emotion = result[0]['dominant_emotion']

                if emotion != last_emotion:
                    print(f"😃 Detected emotion changed: {emotion}")
                    stop_music()
                    play_music(emotion)
                    last_emotion = emotion

                last_detection_time = time.time()
            except Exception as e:
                print("⚠️ Error detecting emotion:", e)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    stop_music()
    print("👋 Exited mood-based music system.")

# Run the system
real_time_mood_music()
