import speech_recognition as sr
import pyttsx3
from os import system # ничего кроме os из библиотеки систем не использовать
micro=sr.Microphone()
r = sr.Recognizer()
engine = pyttsx3.init()

def talk(x):
    engine.say(x) # говорить
    engine.runAndWait() # вслух

talk('Привет мир')

def listen():
    text = ''
    with micro as sourse:
        print('Я Bac слушаю: ')
        r.adjust_for_ambient_noise(sourse)
        audio = r.listen(sourse, phrase_time_limit=3)
        try:
            text = (r.recognize_google(audio, language="ru-RU")).lower()
        except(sr. UnknownValueError):
            pass
        except (TypeError):
            pass
    return(text)

def cmd(text):
    mas = ['джарвис','хэй','арбузы']
    for i in mas:
        text = text.replace(i,'') # удалить лишние слова из списка mas
        text = text.strip() # удаляет лишние пробелы
    if text == 'привет':
        talk('Приветствую вас!')
    if text == 'включи музыку':
        system('D:/music/"Eiffel 65 - Blue.mp3"')

cmd(listen())
input()
