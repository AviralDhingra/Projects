#!/usr/bin/env python3

import os

import pyttsx3
import speech_recognition as sr

from keywordSlicer import identifier

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech


def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # print(voice, voice.id)
    engine.setProperty("rate", 180)
    engine.setProperty('voice', 'english')
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak
name = 'Sir Aviral The Great'
SpeakText(f'Good Morning, {name}')
running = True
while running == True:

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=5)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using ggogle to recognize audio
            MyText = r.recognize_ibm(
                audio2)
            # , show_all=True
            MyText = MyText.lower()
            os.system('clear')
            print(MyText)
            # Caling keywordSlicer Function >> Checks for keyword 'jarvis' + slice string to be only command and not keyword
            MyText = identifier(MyText)
            # When MyText Has keyword in it...
            if MyText != False and MyText != -1:
                finalText = f'Did you say {MyText}'
                print(finalText)
                # SpeakText(finalText)

                if MyText == 'run chrome' or MyText == 'open chrome':
                    os.system('google-chrome')
                elif MyText == 'run calculator' or MyText == 'open calculator':
                    os.system('gnome-calculator')
                elif MyText == 'show apps' or MyText == 'show Applications' or MyText == 'list apps':
                    output = os.system(
                        "dpkg --get-selections | awk '{print $1}'")
                    print(output)
                    # SpeakText(output)
                elif MyText == 'shutdown' or MyText == 'close':
                    os.system('sudo shutdown -h now')
                elif MyText == 'good morning' or MyText == 'good evening' or MyText == 'good night' or MyText == 'hello':
                    mssg = f'{MyText} To You Too Sir'
                    SpeakText(mssg)
                    print(mssg + '!!')
                    # dpkg --get-selections | awk '{print $1}'
                else:
                    if MyText.find('open') != -1 or MyText.find('run') != -1:
                        word = MyText
                        l = word.split(' ')
                        try:
                            l = l[1:]
                            l = ' '.join([str(elem) for elem in l])
                            l = l.replace('dash', '-')
                            l = l.replace('hyphen', '-')
                            l = l.replace(' ', '')
                            l = l.strip()
                            os.system(l)
                        except IndexError:
                            print('Specify Program To Run')

                    """
                    // Not Working... The Spaces (Especially) + Special Charecters Formating Is Different For Every Command
                    word = MyText
                    l = word.split(' ')
                    print(l)
                    print(type(l))
                    l = ' '.join([str(elem) for elem in l])
                    l = l.replace('dash', '-')  # Dash => -
                    l = l.replace('hyphen', '-')  # Hyphen => -
                    l = l.replace('dot', '.')  # Hyphen => -
                    l = l.replace('tilde', '~')  # tilde => ~
                    l = l.replace('slash', '/')  # slash => /
                    # l = l.replace(' ', '')
                    l = l.strip()
                    # l = word.split(' ')
                    print(l)
                    print(type(l))
                    output = os.system(l)
                    """
                    output = os.system(MyText)
                    if output != 0:
                        print(output)
                        txt = 'I Do not understand what you are saying'
                        print(txt + '...')
                        SpeakText(txt)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    # except sr.UnknownValueError:
    #     print("unknown error occured")
    except KeyboardInterrupt:
        mssg = 'Exiting'
        print('[+] ' + mssg + '...')
        SpeakText(mssg)
        os.system('exit')
        os.system('exit')
        running = False
