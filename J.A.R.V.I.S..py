import speech_recognition
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def listen_comand():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            return query
    except speech_recognition.UnknownValueError:
        return 'Damn... Не понял что ты сказал'
def greeting():
    return 'Привет!'

def create_task():
    print('Что добавим в список дел?')
    query = listen_comand()
    with open('todo-list.txt','a') as file:
        file.write(f'{query}\n')
    return f'Задача {query} добавлена в todo-list!'

def main():
    query = listen_comand()
    if query == 'привет друг':
        print(greeting())
    elif query == 'добавить задачу':
        print(create_task())
    else:
        print('Прожуй потом разговаривай!')

if __name__=='__main__':
    main()
