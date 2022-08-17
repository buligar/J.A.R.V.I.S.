import pyttsx3
import os
import random
import webbrowser
import time
import speech_recognition
import speech_recognition as sr
import pandas as pd
from tkinter import *
from fuzzywuzzy import fuzz
from colorama import *
# раздел глобальных переменных
text = ''
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
# r= sr.Recognizer()


engine = pyttsx3.init()
adress =''
j = 0
task_number = 0

ndel = ['джарвис', 'джарвис?','джарвис ты здесь?','джарвис ты здесь', 'ты здесь?', 'ладно', 'не мог бы ты', 'пожалуйста','просыпайся, папочка вернулся','джарвис, проснись']
commands =['привет', 'открой файл', 'выключи комп', 'выруби компьютер', 'пока', 'покажи файл', 'покажи список команд',
'открой vk', 'открой браузер', 'включи vk', 'открой интернет', 'открой уoutube', 'включи музон','вруби музыку', 'очисти файл',
'открой стату', 'покажи статистику', 'открой музыку', 'переведи', 'планы', 'на будущее', 'что планируется']
# раздел описания функций комманд
def pri_com(): # выводит на экран историю запросов
    z = {}
    mas = []
    mas2 = []
    mas3 = []
    mas4 = []
    file = open('commands.txt', 'r', encoding='UTF-8')
    k = file.readlines()
    for i in range(len(k)):
        line = str(k[i].replace('\n','').strip())
        mas.append(line)
    file.close()
    for i in range(len(mas)):
        x = mas[i]
        if x in z:
            z[x] + 1
        if not(x in z):
            b = {x : 1}
            z.update(b)
        if not(x in mas2):
            mas2.append(x)
    for i in mas2:
        mas3.append(z[i])
    for i in range(1, len(mas3)+1):
        mas4.append(str(i)+') ')
    List = pd.DataFrame({
        'command' : mas2,
        'count' : mas3}, index = mas4)
    List.index.name ='№'
    print(List)
def plans():
    global engine
    plans ='''
    Моя задача будет заключаться в помощи в управлении системой умного дома.
    на данный момент ведется работа над виртуальной частыю программного обеспечения.
    Так же ведется работа по оптимизации всех существующих в коде функций.
    в дальнейшем планируется работа над технической частью проекта.
    Она будет состоять из создания эллементов умного дома с помощью микроконтроллеров Аrduino.
    в конечном итоге виртуальная и техническая части проекта будут обьеденены.
    Моя конечная цель будет достигнута.
    '''
    engine.say(plans)

def clear_analis(): # очистка файла с историей запросов
    global engine
    file = open('commands.txt', 'w', encoding = 'UTF-8')
    file.close()
    engine.say('файл аналитики очищен!')
def add_file(x):
    file = open('commands.txt', 'a',encoding = 'UTF-8')
    if x != '':
        file.write(x+'\n')
    file.close()

def comparison(x): # осуществляет поиск самой подходящей под запрос функции
    global commands,j, add_file
    ans = ''
    for i in range(len(commands)):
        k = fuzz.ratio(x, commands[i])
        if (k > 50)&(k > j):
            ans = commands[i]
            j = k
    if (ans != 'пока')& (ans !='привет'):
        add_file(ans)
    return(str(ans))
def web_search(): #осуществляет поиск в интернете по запросу (adress)
    global adress
    webbrowser.open('https://yandex.ru/yandsearch?clid=2028026&text={}&lr=11373'.format(adress))

def check_searching(): # в проверяет нужно-ли искать в интернете
    global text, wifi_name, add_file
    global adress
    global web_search
    if 'найди' in text:
        add_file('найди')
        adress = text.replace('найди','').strip()
        text.replace(adress, '').strip()
        web_search()
        text = ''
    elif 'найди' in text:
        add_file('найди')
        adress = text.replace('найди','').strip()
        text = text.replace(adress,'').strip()
        web_search()
        text =''
    adress = ''

def clear_task(): # удаляет ключевые слова
    global text,ndel
    for z in ndel:
        text - text.replace(z,'').strip()
        text = text.replace('  ',' ').strip()
def hello(): # функция приветствия
    global engine
    z= ['Рада снова вас слышать!', 'что вам угодно?', 'Привет. Чем-нибудь помочь?']
    x = random.choice(z)
    engine.say(x)

def quit(): # функция выхода из програмны в1obal
    global engine
    x=['надеюсь мы скоро увидемся!', 'рада была помочь', 'всегда к вашим услугам']
    engine.say(random.choice(x))
    engine.runAndWait()()
    engine.stop()
    os.system('cls')
    exit(0)
    raise SystemExit

def show_cmds():  # выводит на экран список доступных комманд
    my_com = ['привет', 'открой файл', 'выключи комльютер', 'пока', 'покажи список команд',
              'открой vk', 'открой интернет', 'открой уoutube', 'включи музыку', 'очисти файл', 'покажи статистику']
    for i in my_com:
        print(i)
    time.sleep(2)

def brows():  # открывает браузер
    webbrowser.open('https://google.ru')


def ovk():  # открывает вк
    webbrowser.open('https://vk.com/feed')


def youtube(): #открывает ютуб
    webbrowser.open('https://www.youtube.com')

def shut():  # ыключает компьютер
    global quit
    os.system('shutdown /s /f /t 10')
    quit()

def musik(): # включает музыку
   webbrowser.open('https://vk.com/audios296431501')
def check_translate():
    global text, tr
    tr = 0
    variants = ['переведи', 'перевести', 'переводить', 'перевод']
    for i in variants:
        if (i in text)&(tr == 0):
            word = text
            word = word.replace('переведи', '').strip()
            word = word.replace('перевести', '').strip()
            word = word.replace('переводить', '').strip()
            word = word.replace('перевод', '').strip()
            word = word.replace('слово', '').strip()
            word = word.replace('слова', '').strip()
            webbrowser.open('https://translate.google.ru/#view=home&op=translate&sl=auto&tl=ru&text={}'.format(word))
            tr = 1
            text = ''
cmds = {
        'привет' : hello,
        'пока' : quit,
        'открой браузер' : brows,
        'открой уoutube' : youtube,
        'открой стату' : pri_com,
        'покажи файл' : pri_com,
        'планы' : plans,
        'выруби компыютер' : shut,
        'покажи статистику' : pri_com,
        'включи vk' : ovk,
        'вруби музыку' : musik,
        'включи музон' : musik,
        'открой файл' : pri_com,
        'на будущее' : plans,
        'выключи комп' : shut,
        'покажи список команд' : show_cmds,
        'открой интернет' : brows,
        'открой vk' : ovk,
        'очисти файл' : clear_analis,
        'открой музыку' : musik,
        'что планируется' : plans,
        'переведи' : check_translate
}

def talk():
    global text, clear_task
    text = ''
    """The function will return the recognized command"""
    print('Слушаю...')
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            text = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
    except speech_recognition.UnknownValueError:
        return 'Damn... Не понял что ты сказал :/'
    # with sr.Microphone() as sourse:
    #     print('я вас слушаю: ')
    #     r.adjust_for_ambient_noise(sourse)
    #     audio = r.listen(sourse, phrase_time_Limit=3)
    #     try:
    #         text = (r.recognize_google(audio, Language='ru-RU')).lower()
    #         print(text)
    #     except(sr.UnknownvalueError):
    #         pass
    #     except(TypeError):
    #         pass
    #     os. system('cls')
    #     lb['text'] = text
    #     clear_task()


def cmd_exe():
    global cmds, engine, comparison, check_searching, task_number, text, lb
    check_translate()
    text = comparison(text)
    print(text)
    check_searching()
    if (text in cmds):
        if (text != 'привет') & (text != 'пока') & (text != 'покажи список команд'):
            k = ['Секундочку', 'Сейчас сделаю', 'уже выполняю']
            engine.say(random.choice(k))
        cmds[text]()
    elif text == '':
        pass
    else:
        print('Команда не найдена!')
    task_number += 1
    if (task_number % 10 == 0):
        engine.say('y вас будут еще задания?')
    engine.runAndWait()
    engine.stop()
# исправляет цвет
print(Fore.YELLOW + '',end ='')
os.system('cls')

# основной бесконечный цикл
def main():
    global text, talk, cmd_exe, j
    try:
        talk()
        if text != '':
            cmd_exe()
            j = 0
    except(UnboundLocalError):
        pass
    except(TypeError):
        pass


# раздел создания интерфейcа
# root = Tk()
# root.geometry('250x350')
# root.configure(bg='gray22')
# root.title('Sara')
# root.resizable(False, False)
#
# lb = Label(root, text=text)
# lb.configure(bg='gray')
# lb.place(x=25, y=25, height=25, width=200)
# but1 = Button(root, text='Cлушать', command=main)
# but1.configure(bd=1, font=('Castellar', 25), bg='gray')
# but1.place(x=50, y=160, height=50, width=150)
# but2 = Button(root, text='Выход', command=quit)
# but2.configure(bd=1, font=('Castellar', 25), bg='gray')
# but2.place(x=50, y = 220, height = 50, width = 150)
# root.mainloop()
while True:
    main()