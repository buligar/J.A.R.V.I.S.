import speech_recognition as sr
import pyttsx3
from fuzzywuzzy.fuzz import ratio as rt
from os import system

micro = sr.Microphone()
r = sr.Recognizer()
engine = pyttsx3.init()

def talk(x):
    engine.say()
    engine.runAndWait()

def listen():
    text = ''
    print('Я вас слушаю:')
    while text == '':
        with micro as source:
            #r.adjust_for_ambient_noise(source)
            audio = r.listen(source,phrase_time_limit=3)
            try:
                text = (r.recognize_google(audio,language="ru-RU")).lower()
            except(sr.UnknownValueError,TypeError):
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
        ('привет','приветствую','здарова'): hi,
        ('пока','прощай','уйди','не мешай','отстань'): bye
    }
    maintask = ''
    koof = 0
    for i in cmds:
        for k in i:
            if (rt(k,text)>70)&(rt(k,text)>koof):
                maintask = i
                koof = rt(k,text)
    if maintask in cmds:
        cmds[maintask]()
    else:
        pass
while True:
    try:
        cmd_exe(listen())
    except KeyError: # если случается ошибка KeyError то пропускаем
        pass