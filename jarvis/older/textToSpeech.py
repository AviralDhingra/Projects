import pyttsx3

name = 'Sir Aviral The Great'
inp = f'Good Morning, {name}'
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voice, voice.id)
engine.setProperty("rate", 150)
engine.setProperty('voice', 'english')
engine.say(inp)
engine.runAndWait()
engine.stop()

print(engine.getProperty('voice'))
