import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
SPEECH_RATE = 150
engine.setProperty('rate', SPEECH_RATE)

def say_text(text):
    engine.say(text)
    engine.runAndWait()

def get_audio_input(prompt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        say_text(prompt)
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=10)
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            say_text("Could not understand audio. Please try again.")
        except sr.RequestError:
            say_text("Speech service error. Please try again.")
    return None

