import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from playsound import playsound
import os

def SpeakText(reply, language='en', accent = 'co.uk'):
    text = reply
    myobj = gTTS(text=text, tld=accent, lang=language, slow=False)
    myobj.save("welcome.mp3")
    playsound("welcome.mp3")
	
	
def speech_to_text():
    microphone = sr.Microphone(device_index=6)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        voice_rec = r.recognize_google(audio, language = 'en-IN', show_all = True)
        command = voice_rec['alternative'][0]['transcript']
        return command, voice_rec
            
    

# while(1):
#     cmd, voice_rec = speech_to_text()
#     print(f'\n{cmd}\n')
#     print(cmd)
#     SpeakText(f'Did you say {cmd}?')

SpeakText('Good Afternoon Sir Aviral The Great')
os.system('google-chrome')

