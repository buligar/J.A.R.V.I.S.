import speech_recognition as sr
import pyttsx3
from os import system

micro = sr.Microphone()
r = sr.Recognizer()
engine = pyttsx3.init()

def talk(x):
    engine.say()
    engine.runAndWait()

def listen():
    text = ''
    with micro as source:
        print('Я вас слушаю:')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,phrase_time_limit=3)
        try:
            text = (r.recognize_google(audio,language="ru-RU")).lower()
        except(sr.UnknownValueError):
            pass
        except(TypeError):
            pass
    return(text)

def cmd_exe(text):
    task = ''
    mas = ['джарвис','пожалуйста']
    for i in mas:
        text = text.replace(i,'')
        text = text.replace('  ',' ')
    text = text.strip()
    def hi():
        global talk
        talk('приветсвую вас! как дела?')
    def bye():
        global talk
        talk('удачного дня!')
        exit()
    cmds = {
        'hello':('привет', 'здарова','приветствую'),
        'bye': ('пока','прощай','свали')
    }
    exe = {
        'hello': hi,
        'bye': bye
    }
    for i in cmds:
        for k in cmds[i]:
            if text == k:
                task = i

    exe[task]()

while True:
    try:
        cmd_exe(listen())
    except KeyError: # если случается ошибка KeyError то пропускаем
        pass