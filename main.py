import speech_recognition as sr
# to direct 
import webbrowser
# to convert text to speech
import pyttsx3
 
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

def processCommand(c):
    # print(c)
    if c.lower() == "open google":
        webbrowser.open("https://google.com")
    if c.lower() == "open youtube":
        webbrowser.open("https://youtube.com")
    if c.lower() == "open linkedin":
        webbrowser.open("https://linkedin.com")
    if c.lower() == "open chatgpt":
        webbrowser.open("https://chatgpt.com")
    if c.lower() == "open whatsapp":
        webbrowser.open("https://whatsapp.com")

if __name__ == "__main__":
    speak("Installing Jarvis....")
    #Listen for the wake word jarvis
    while True:
        # Listen for "Jarvis"
        #  obtain audio from microphone
        r = sr.Recognizer()

        print("Recognizing....")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening....")          
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            # print(command)
            if(word.lower() == "jarvis"):
                speak("Hello i am jarvis, how can i help you")
                with sr.Microphone() as source:
                    print("Jarvis Active....")          
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)
                    commmand = r.recognize_google(audio)

                    processCommand(commmand)
        except Exception as e:
            print (e)
