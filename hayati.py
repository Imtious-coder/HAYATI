import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
  engine.say(audio)


if __name__ == "__main__":
  speak("Hayati repoting sir")