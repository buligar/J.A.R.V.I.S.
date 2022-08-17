import speech_recognition as sr, time
from win32com.client import Dispatch as d
from fuzzywuzzy import fuzz
from os.path import abspath as tdir
from random import choice
from colorama import *
from os import system
class Assistent:
    def __init__(self):
        self.cmds = {
                ('не мешай', 'уйди', 'свали', 'отвали', 'я ушел', 'пока') : self.hi, #self.bye,
                ('здаров', 'привет', 'здравствуй') : self.hi, #self.hello,
                ('поздоровайся', 'поприветствуй гостей'): self.hi, #self.greet,
                ('как дела', 'что делаешь') : self.hi,
                ('спасибо', 'молодец', 'благодарю') : self.hi, #self.thanks,
                ('завершай работу', 'давай спать', 'выруби систему', 'выруби всё'): self.hi, #self.shuting,
                ('защита', 'защиту', 'блокировка', 'заблокируйся', 'сон', 'заблокируй экран') : self.hi, #self.lock,
                ('открой уoutube','зайди на уоutube', 'включи уoutube', 'вруби уoutube') : self.hi,
                ('выключи браузер','закрой браузер', 'выруби браузер') : self.hi,
                ('выключи музыку', 'выруби музыку', 'тишe', 'музыку выключи','музыку выруби') : self.hi,
                ('новости', 'какие новости', 'новости на сегодня', 'что нового') : self.hi, #self.show_news,
                ('найди', 'найти') : self.hi, #self.web_search,
                ('расскажи', 'объясни', 'скажи', 'подскажи') : self.hi, #self.talLker,
                ('день недели','какой день недели', 'какой сегодня день недели') : self.hi,
                ('сколько время', 'время', 'сколько времени') : self.hi, #self.tim,
                ('число','какое сегодня число', 'какое число') : self.hi,
                ('повтори', 'ещё раз', 'повторить ещё раз', 'повтори ещё раз', 'ну ка ещё раз', 'ну ка повтори ') : self.hi, #self.repeat,
                ('установи соединение', 'соеденись с ардуиной', 'установи соединение с ардуиной', 'обнови ардуину', 'перезагрузи ардуину') : self.hi, #self.connect,
                ('включи свет', 'вруби свет') : self.hi, #self.on_3,
                ('выключи свет', 'выруби свет') : self.hi, #self.off_3,
                ('шифрование', 'кодирование') : self.hi, #self.shif
        }
        self.keywords = ['включи',
                         'выключи',
                         'найди',
                         'открыть',
                         'здаров',
                         'свали',
                         'выключай',
                         'найти',
                         'расскажи',
                         'здравствуй',
                         'включай',
                         'отключи',
                         'открывай',
                         'скажи',
                         'поздоровайся',
                         'вруби',
                         'отключай',
                         'запусти',
                         'объясни',
                         'поприветствуй',
                         'врубай',
                         'открой',
                         'запускай',
                         'рассказывай',
                         'добавь',
                         'подключи',
                         'вырубай',
                         'запустить',
                         'объясняй',
                         'удали',
                         'подключай',
                         'отруби']
        self.double_keys = [['как','дела','что','делаешь']]

        self.r = sr.Recognizer()
        self.r.pause_threshold = 1
        self.m = sr.Microphone()
        with self.m as self.sourse:
            self.r.adjust_for_ambient_noise(self.sourse)
        self.engine = d("SAPI.SpVoice")
        self.mode = 'standard'

    def hi(self):
        print('Hi!')
    def talk(self, text):
        self.engine.Speak(text)

    def first_ans(self):
        vals = ('я вас слушаю', 'да - да', 'к вашим уcлугам')
        self.talk(choice(vals))

    def listen(self):
        system('cls')
        text = ''
        print(choice((Fore.GREEN, Fore.WHITE, Fore.YELLOW)) + 'Я ВАС СЛУШАЮ:')

        while text =='':
            with self.m as self.sourse:
                audio = self.r.listen(self.sourse)
                try:
                    text = (self.r.recognize_google(audio, language="ru-RU")).Lower()
                except:
                    pass

        if text in ('эй', 'сара', 'ты здесь', 'ты тут', 'слышь', 'слышишь', 'сара ты тут', 'сара ты здесь'):
            self.first_ans()
            return ''
        else:
            return (text)

    def clear_cmd(self, global_task):
        def clear_cmd3(k):
            tasks=[]
            task=''
            if len(k.split()) < 2:
                return [k]
            else:
                if k != '':
                    k.split()
                    for i in range(-1, len(k)-2):
                        if (i+1 == len(k) -2):
                            if k[i+2]:
                                task = f'{task} {k[i+1]} {k[i+2]}'
                            else:
                                task = f'{task} {k[i+1]}'
                            tasks.append (task.strip())
                        else:
                            for j in range (len (self.keywords)):
                                if (fuzz.ratio (k[i+1], self.keywords[j]) > 80):
                                    tasks.append (task.strip())
                                    task = ''
                                    break
                            if k[i+2]:
                                task = f'{task} {k[i+1]} {k[i+2]}'
                            else:
                                task = f'{task} {k[i+1]}'
                    for i in range (len (tasks)):
                        task=tasks[i].split()
                        for dl in ('уйди', 'свали'):
                                if task:
                                    if fuzz.ratio(task[-1], dl) > 70:
                                        (tasks[i].replace(task[-1], '')).strip()
                                        tasks[i] = tasks.append ('не мешай')

                        if task:
                            if fuzz.ratio(task[-1], 'мешай') > 80:
                                if fuzz.ratio(task[-2], 'нe') > 80:
                                    tasks[i] = (tasks[i].replace(task[-1], '')).strip()
                                    tasks[i] = (tasks[i].replace(task[-2], '')).strip()
                                    tasks[i] = tasks.append ('не мешай')


                    for i in range(len(tasks)):
                        if tasks[i].endswith(' и'):
                            ntask = tasks[i].split()
                            del ntask[len(ntask) - 1]
                            tasks[i] = (' '.join(ntask))
                    for i in range(len(tasks)):
                        if tasks[i].split():
                            if fuzz.ratio(tasks[i].split()[-1], 'потом') > 80:
                                ntask = tasks[i].split()
                                del ntask[-1]
                                tasks[i] = ' '.join(ntask)

                    if (tasks and k):
                        tasks[-1] = f'{tasks[-1]} {k[-1]}'
                    return list(filter(None, tasks))

        def main(k):
            new_list = clear_cmd3(k)
            taskss = []

            for task in new_list:
                var = clear_cmd3(task)
                for i in var:
                    taskss.append(i)
            new_list = []
            for task in taskss:
                var = clear_cmd3(task)
                for i in var:
                    new_list.append(i)
            taskss = []

            for task in new_list:
                task = task.split()
                if len(task) == 1:
                    taskss.append(" ".join(task))
                else:
                    n_task = ''
                    for var in range(len(task)):
                        if (task[var] in self.keywords):
                            taskss.append(n_task.strip)
                            n_task = task[var]
                        elif (var == len(task) - 1):
                            n_task = f'{n_task}{task[var]}'
                            taskss.append(n_task.strip())
                        else:
                            n_task = f'{n_task}{task[var]}'
            return [value for value in taskss if value]

        def delete_doubles(ans):
            for task in range(len(ans)):
                wars = []
                last = ''
                var = ans[task].split()
                for word in var:
                    if word == last:
                        wars.append(word)
                    last = word
                ans[task] = ' '.join(wars)
            return ans

        def delete_doubles2(ans):
            last = ''
            tasks = ans
            ans = []
            for task in tasks:
                if task + last:
                    ans.append(task)
                    last = task
                else:
                    pass
            return ans


        def task_interpreter(ans):
            def get_pairs(task):
                double_keys = [['как', 'дела'],
                               ['что', 'делаешь' ]]
                ans = []
                flag = 0
                for double in double_keys:
                    pairs = [' '.join(double).strip(), ''.join(double[::-1]).strip()]
                    for pair in pairs:
                        if  pair in task:  # ecли пара есть в запросе
                            flag = 1
                            var = task.replace(pair, '').strip()
                            if task.startswith(pair):
                                ans.append([pair, var])
                            elif task.endswith(pair):
                                ans.append([var, pair])
                    if flag == 0:
                        ans.append(task)
                    return ans

            def rearkh(mas):
                def rearkh_cycle(ans):
                    nans = ans
                    ans = []
                    for val in nans:
                        if type(val) == list:
                            for i in val:
                                ans.append(i)
                        else:
                            ans.append(val)
                    return ans

                def check(mas):
                    flag = 0
                    for val in mas:
                        if type(val) == list:
                            flag = 1
                    return flag
                while check(mas):
                    mas = rearkh_cycle(mas)
                return mas
            for i in range(len(ans)):
                ans[i] = get_pairs(ans[i])
            return rearkh(ans)

        ans = delete_doubles(main(global_task))
        ans = delete_doubles2(task_interpreter(ans))
        n_ans = [x for x in ans if not (x in self.keywords)]
        ans = []
        for task in n_ans:
            if task.endswith(' и'):
                task = (task[:: -1].replace('и ', '', 1))[::-1]
            if task.startswith('и '):
                task = task.replace('и ', '', 1)
            for i in ['сначала', 'потом', 'давай', 'сделай', 'старая', 'ладно']:
                if ((i in task) and (not (task.split()[0] in ['найди', 'расскажи', 'добавь', 'удали']))):
                    task = task.replace(i,' ').strip().replace('  ', '')
                if fuzz.ratio(task, 'capa') < 70:
                    task = task.replace('capa', ' ').strip()
            ans.append(task.strip().replace('  ', ''))
        if 'capa' in ans:
            if len(ans) > 1:
                del ans[ans.index('capa')]
        return ans

    def cmd_exe(self, tasklist):

    #реализовать многопоточность

        def search_exe_function(task):
            return None
        for task in tasklist:
            print(task)

    def run(self):
        self.cmd_exe(self.clear_cmd(input('>>> ')))

assistent = Assistent()
while True:
    assistent.run()