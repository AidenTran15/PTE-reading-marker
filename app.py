import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)
    try:
        print('Analyzing...')
        query = r.recognize_google(audio, language='en-in', key='AIzaSyCR-rKfodcJxRcCZd9XQa_20UR2p3ltV1Y')
        #print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        print('Sorry I dont understand')
        query = str(input('Command: '))

    return query

if __name__ == '__main__':
    print('Please start speaking...')

    query = myCommand()

    print('This is what you just said: ', query)

