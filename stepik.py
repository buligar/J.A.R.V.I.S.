###1
# a=[int(i) for i in input().split()]
# b=int(input())
# d=[]
# if b in a:
#     for i in enumerate(a):
#         if i[1] == b:
#             d += [i[0]]
#     for val in d:
#         print(val, end=' ')
# else:
#     print('Отсутствует')

###2
# n=int(input())
# m=int()
# for i in range(n*n):

###3
# def f(x):
#     if x<=-2:
#         m=1-(x+2)**2
#     elif -2<x<=2:
#         m=-x/2
#     elif x>2:
#         m=((x-2)**2)+1
#     return m

###4

# lst = [1, 2, 3, 4, 5, 6]
# def modify_list(l):
#     for i in range(len(l)):
#         if l[i]%2:
#             list[:]=l[i]/2
#         else:
#             i+=1
#         return m
#
# modify_list(lst)
# print(lst)
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]


###5

# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     elif 2*key in d:
#         d[2*key].append(value)
#     else:
#         d[2*key]=[]
#         d[2*key].append(value)
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}

###6

# list = input().lower().split()
# unique = []
# for i in set(list):
#     print("{} {}".format(i, list.count(i)))

###7

# digits = set('0123456789')
# i = 0
# multiplier = ''
# decrypted = ''
#
# with open('dataset_3363_2 (3).txt') as in_f_obj:
#     string = in_f_obj.readline().strip()
#
# char = string[i]
# i += 1
#
# while i < len(string):
#
#     while string[i] in digits:
#         multiplier += string[i]
#         i += 1
#         if i > (len(string) - 1):
#             break
#
#     # print(char * int(multiplier), end='')
#     decrypted += (char * int(multiplier))
#
#     multiplier = ''
#     if i > (len(string) - 1):
#         break
#     char = string[i]
#
#     i += 1
#
# with open('123.txt', 'w') as out_f_obj:
#     out_f_obj.write(decrypted)

###8

# dictionary={}
# with open('data.txt') as in_f_obj:
#     for line in in_f_obj:
#         line = line.lower()
#         print(line)
#         for word in line.split():
#             if word not in dictionary:
#                 dictionary[word] = 1
#             elif word in dictionary:
#                 dictionary[word] += 1
#
# max_quantity = 1
#
# for key, value in dictionary.items():
#     current_quantity = dictionary[key]
#     print(current_quantity)
#     if current_quantity > max_quantity:
#         max_quantity = current_quantity
#         word_with_max_quantity = key
#         print(word_with_max_quantity)
#         print(max_quantity)
#
# with open('output.txt', 'w') as out_f_obj:
#     most_popular = (word_with_max_quantity.upper() + ' ' + str(max_quantity))
#     out_f_obj.write(most_popular)

# import glob
#
# for name in glob.glob("C:\\Users\\bulig\\.keras\\datasets\\PBC_dataset_normal_DIB\\**.jpg"):
#    print(open(name))

# import os
# import shutil
# from PyQt5.QtWidgets import QFileDialog
# path='C:\\Users\\bulig\\.keras\\datasets\\test'
# papka=[]
# files_names=[]
# i=0
# q=0
# list = os.listdir('C:\\Users\\bulig\\.keras\\datasets\\test')
# file_count = len(list)
# for k in range(file_count):
#    for p in os.listdir(path):
#       full_path = os.path.join(path, p)
#       a=[full_path]
#       papka+=a
#       i+=1
#
#    for j in os.listdir(papka[k]):
#       full_path = os.path.join(path, j)
#       # os.path.isfile(full_path)
#       a=[full_path]
#       files_names+=a
#       q+=1
#    print(files_names)
#    print(q)
#    file_oldname = os.path.join("C:\\Users\\bulig\\PycharmProjects\\pythonProject", "glcm_all.csv")
#    file_newname_newfile = os.path.join("C:\\Users\\bulig\\PycharmProjects\\pythonProject", f"glcm_train{k}.csv")
#    os.rename(file_oldname, file_newname_newfile)


# import requests
# r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/843785.txt')
# a=r.text
# ouf = open('file.txt', 'w')
# ouf.write(a)

import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)
        data={
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]':response.get('country'),
            '[Region name]':response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon')
        }
        for k,v in data.items():
            print(f'{k}:{v}')
        area = folium.Map(location=[response.get('lat'),response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('Please enter a target IP:')

    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()
