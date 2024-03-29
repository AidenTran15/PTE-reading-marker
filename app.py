import pyttsx3
import speech_recognition as sr
from sources import paragraphs
import random
import json

crediential = {
  "type": "service_account",
  "project_id": "learnraise-235507",
  "private_key_id": "c3db04a6871c6bde026eb0ad99fa71022c1679e6",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCikBLYUK6EyWUq\nQPupY9WbIvZTCNsLrkpvLx2VlehqS16soF0c39luEfTn3MQ0FPVZlVA8pfCRgqrL\nMVtMrPTlpS87Okg0TTgNUlcs93jHBLPk14yfyC4H7JgMYR5ZHuMycyNFle835+3F\nr8ecpPcoM31/JFx6aREr1K/moxUKvLV7MUW4TaqPMvyUn/ielGm0Tg50111JDi6/\n1yEabywJZf3TAF1eQXHY0BssrL4uNN+avpcIKUQkSYNF+/f+zVor0JXJrpX1hXf0\noVzWwf8EYh7lvRNQXUljJVmSo7Hmaq39yKU8dUEPtr7eNdvfXOXGMFk4YwXqUfBo\nk69wxIsfAgMBAAECggEAP9cGn46nypvwr7RPYIlFVKRZSeibZS3wK1O8cYcqe7vX\nlUFw76r1D2Xb4MZxAucMJz8dAIRGQk6nVh6u9SCjGCBTuRW9T1TX41tnws/4zWeK\nYh9IKWOKuC/w0kO9kFAx9xkCTAyColjhppXOdTTPnykBatHTw3rJdIYVAiUfWVR8\nLcITwtSGX+wNd5z833IgHJmhptKlS+ceXun6kZMqPhsi5I6vyv/x+YZziFY17I/q\n6atv2TMZkltasqAvYEKdzl5o3KJrYoVVYq53YsiHKjllqYAOdaE8CM8iWO7r/G45\neUU1u1iTjwTs8YGr8kT+EaSPvycx5aQusqUcrr2eCQKBgQDUzencVnIEVENf4aIc\nf4gWfj+Jsu68/J3BdCRB6FxLo5+YstKurfXUXa9VFsoYgsGkgEfasrN0kr2ib48P\n0yQMIbgg4dPvaptfyR51cF5uQa8bwRrdSRbD8Joiq4fapGaW1hA0nvmqx4UBVjxd\n9EJOU1BPmskBnJ15XW5Sur0mxQKBgQDDj20YRGw0JXJbx6qcSd53AybV/4amOK5F\n8ioUPwRizAiwtEzK2eAe5MnO//mkOEIWz8zFI+0BVm748FaBu/qmG7gUgteEYtJh\n2wDwUdmGVC9gu7fJNsEjcQUwrOhTzEELknt3V/Yzqe+2zYa2Kv4ZxmHHgyJEZGcV\n8eSa/T6okwKBgQCdYGcKFzgc8YAeIYy1DK/FCrrMh/K8+wlj7xN9Vm0jVy+JSv46\nRtadpmcrQz5UYCb7FA+Pska6+GacAWrIpjpramh0kO4eijW74c3Pxjlfyt3IZcgL\nTKk0YPRsnXRMAvcHp+m2MLetT/6SHYdpaGG88SpcpLjwozVmcu1K62VFjQKBgF3v\nbv/RHgiOVDgx2InqEaopIWZ5rzv4zf1bLUs8Web7CtGWSazGqxkr3KRJ4Kg5PcWn\nWzz23Mlfsz5wc50tpmBTwEBZ+RvmPBg1EmZdapdTqM5WXRmR64QSreOLqq1V14iv\nfA7/eYunfTXZ03N9g0DuQdmL69HeSIYKAz1Pl+FxAoGAf/q0EyBjxedyFv+6cYkf\nrKUMO7tk+JYDZV9zI8yzQEtEF0L9I6E30SOehmhBopOoqVB2kFxf9dxd3U0QsRo+\nSSYQc5lZuJ6UDV3xzVLgsa0LNjnZT0WobrX9J/Dd15VayxD67QuT1v0McW3h93j7\n/ArDwuB+ogMCQA2bROAPDHg=\n-----END PRIVATE KEY-----\n",
  "client_email": "pte-maker@learnraise-235507.iam.gserviceaccount.com",
  "client_id": "100940238298974669510",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/pte-maker%40learnraise-235507.iam.gserviceaccount.com"
}


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def myCommand():
    # Record the user's voice
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        r.pause_threshold = 3
        audio = r.listen(source)
    # Send the audio to Google to convert into text
    try: 
        print('Analyzing...')
        query = r.recognize_google_cloud(audio,credentials_json= json.dumps(crediential), language='en-US');
        
    except sr.UnknownValueError:
        print('Sorry I dont understand')
        query = str(input('Command: '))
    
    return query

if __name__ == '__main__':
    print("Instruction: You will be presented with a paragraph, start reading that paragraph when you see the message 'Please start speaking...'")
    #Calculate the numnber of pragraphs
    num_of_paragraph = len(paragraphs)
    #Generate a random index
    randomNumber = random.randint(0, num_of_paragraph-1 )
    
    paragraph =  paragraphs[randomNumber]
    print('Testing paragraph: ', paragraph)

    print('Please start speaking...')

    userInput = myCommand()

    print('This is what you just said: ', userInput)
    
    splitParagraph = paragraph.split()
    splitUserInput = userInput.split()
    total = len(splitParagraph)
    countCorrect = 0
    
    for i in range(len(splitUserInput)):
        if splitParagraph[i] == splitUserInput[i]:
            countCorrect += 1
    print(str(countCorrect/total*100)+"%")