import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def takeCommand():   
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'Alexa' in command:
                actual_command = command.replace('Alexa', '')
                print(actual_command[1:])

    except:
        pass

    return actual_command

def removePrefix(text, prefix):
    return text[len(prefix):]

def main():
    while True:
        command = takeCommand()
        if 'play' in command:
            song = removePrefix(command.replace('play', ''), '  ')
            talk('ok, playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk("Current time is " + time)

        else:
            talk("Ok, quitting")
            return False
        
if __name__ == "__main__":
    main()
