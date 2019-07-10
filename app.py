import pyttsx3
import speech_recognition as sr
from sources import paragraphs
import random

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
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
    print("Instruction: You will be presented with a paragraph, start reading that paragraph when you see the message 'Please start speaking...'")
    num_of_paragraph = len(paragraphs)
    randomNumber = random.randint(0, num_of_paragraph-1 )
    print('Testing paragraph: ', paragraphs[randomNumber])

    print('Please start speaking...')

    query = myCommand()

    print('This is what you just said: ', query)

