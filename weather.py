import pyowm
token='c8a1bcee74a832dc895e5f518ce57d72'
owm = pyowm.OWM(token)
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Москва')
w = observation.weather
temp = w.temperature('celsius')

date = observation.reception_time(timeformat='iso')
print(date)

print('Облачность',w.clouds,'%')
print('Влажность',w.humidity,'%')
print(temp['temp'])
print(w.status)
input()
