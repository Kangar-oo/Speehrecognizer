import pyttsx3
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening...")

    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)

    # Capture the audio input
    audio = recognizer.listen(source)

    print("Recognizing...")

    try:
        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
