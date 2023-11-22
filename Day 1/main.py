import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice',Id)
    print("")
    print(f"==> ISO AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

    try:
        print("Recogizing....")
        query = r.recognize_google(audio,language="en")
        print(f"==> Ahmad : {query}")
        return query.lower()

    except:
        return ""
    
def MainExecution(query):
    Query = str(query).lower()

    if "hello" in Query:
        speak("Hello Sir, Welcome Back!")
    
    elif "bye" in Query:
        speak("Nice to meet you sir, Have a nice day!")

while True:
    print("")
    Query = speechrecognition()
    MainExecution(Query)
