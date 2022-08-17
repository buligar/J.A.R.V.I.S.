import speech_recognition as sr
import webbrowser as wb
r =sr.Recognizer()

def listen():
    text = ''
    with sr.Microphone() as sourse:
        print('Я вас слушаю:')
        r.adjust_for_ambient_noise(sourse)
        audio = r.listen(sourse)
        try:
            text = (r.recognize_google(audio,language="ru-RU")).lower()
        except:
            pass
    print(f"Вы сказали: {text}")
    return(text)
def exe(task):
    mas = ['джарвис','пожалуйста','давай']
    keys = ('найди','найти','ищи')
    for i in mas:
        task = task.replace(i,'') # удаляем слова из списка mas
        task = task.replace('  ',' ')
    task = task.strip() # удалить пробелы в начале и в конце
    input(task)
    for i in keys:
        if i in task:
            zapros = task.replace(i,'')
            zapros = zapros.strip()
            task = 'найди'
    if task == 'найди':
        wb.open(f'https://www.google.com/search?q={zapros}&oq=%{zapros}%81&aqs=chrome..69i57j0i512l2j46i131i433i512j0i512l6.1318j1j15&sourceid=chrome&ie=UTF-8')


while True:
    exe(listen())
