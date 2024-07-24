import pyttsx3 
import speech_recognition as sr

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def one():
    f = open("Genghis Khan.txt","r")
    for j in f:
        j.lower()
        print(j)
        speak(j)
    f.close()

def two():
    f = open("Peter Rabbit.txt","r")
    for j in f:
        j.lower()
        print(j)
        speak(j)
    f.close()
        
def command():
    while True:
        r = sr.Recognizer()
        # needs pyaudio as PyAudio-0.2.11-cp38-cp38-win32.whl
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing....")
            q = r.recognize_google(audio, language = "en-in")
            print(q)
            
        except Exception as e:
            print(e)
            return "None"

        return quit

if __name__=="__main__":
    while True:
        speak("which one shall i read")
        q = command()
        if 'a' in q:
            one()
        elif 'b' in q:
            two()
