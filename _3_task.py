print('easy / Задание - 1:\n')
# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
name = input('Введите имя: ')
age = input('Введите возраст: ')
town = input('Введите город: ')

def some_function(name, age, town):
    print('{}, {} год(а), проживает в городе {}'.format(name, age, town))

print(some_function(name, age, town))

print('\neasy / Задание - 2:\n')
# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
x, y, z = 1, 2, 3
def maxim(x, y, z):
    return max(x, y, z)

print(maxim(x,y,z))

print('\neasy / Задание - 3:\n')
# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
str1, str2, str3 = 'a', 'bb', 'ccc'

def longest(*args):
    length = 0
    for i in [*args]:
        if len(i) > length:
            length = len(i)
            longest_string = i
    return i
print(longest(str1, str2, str3))

print('\nnormal / Задание - 1:\n')
# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

# формирую списки, создаю словарь
names = ['Иван Иванов', 'Василий Васильев', 'Максим Максимов', 'Никита Никитин']
salary = [100000, 300000, 450000, 900000]
dct = dict(zip(names, salary))

# по условиям задачи не понял, надо ли писать в файл в результат, поэтому написал функцию записи в файл:
def dict_to_file(file, dictionary):
    with open(file, 'w') as fout:
        for key in dictionary.keys():
            fout.write('%s - %s\n' % (key,dictionary[key]))

# записываю в файл
dict_to_file('salary.txt', dct)

# читаю из файла
salary_read = []
with open('salary.txt') as file:
    lines = file.readlines()
# строки парсю в элементы, кидаю в словарь
for i in lines:
    i = i.split(' - ')
    salary_read.append(i)
dct_read = dict(salary_read)

# вывожу результат с уловиями задачи
dct_cleared = list()
for key, value in dct_read.items():
    if int(value) < 500000:
        dct_cleared.append([key.upper(), int(value)*0.87])
        print(key.upper(), int(value)*0.87)
dct_cleared = dict(dct_cleared)

# не понял, надо ли записывать, поэтому спрашиваю, нужна ли запись в файл:
request = input('Нужно ли записать результаты в файл (y/n)?')
if request == 'y':
    dict_to_file('output.txt', dct_cleared)

print('\nhard / Задание - 1:\n')

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

player_name = input('Введите имя player: ')
enemy_name = input('Введите имя enemy: ')

player = {'name' : player_name,
         'health' : 100,
         'damage' : 50}
enemy = {'name' : enemy_name,
         'health' : 150,
         'damage' : 30}

def attack(person1, person2):
    person1['health'] = person1['health'] - person2['damage']
attack(player, enemy)
print('player health: ', player['health'])

print('\nhard / Задание - 2:\n')

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

# начну с генерации статистик - предлагаю либо забить их пользователю, иначе генерирую случайно

import random
import time

player_name = input('Введите имя player: ')
enemy_name = input('Введите имя enemy: ')
request = input('Хотите ли Вы сами ввести характеристики(y/n): ')
if request == 'y':
    player_health = int(input('player health (целое число): '))
    player_damage = int(input('player damage (целое число): '))
    player_armor = round(float(input('player armor (дробное число): ')), 1)
    enemy_health = int(input('enemy health (целое число): '))
    enemy_damage = int(input('enemy damage (целое число): '))
    enemy_armor = round(float(input('enemy armor (дробное число): ')), 1)
    player = {'name' : player_name,
              'health' : player_health,
              'damage' : player_damage,
              'armor' : player_armor}
    enemy = {'name' : enemy_name,
              'health' : enemy_health,
              'damage' : enemy_damage,
              'armor' : enemy_armor}
else:
    player = {'name' : player_name,
              'health' : random.randrange(50, 200),
              'damage' : random.randrange(5, 51),
              'armor' : round(random.uniform(1.0, 1.9), 1)}
    enemy = {'name' : enemy_name,
              'health' : random.randrange(50, 200),
              'damage' : random.randrange(5, 51),
              'armor' : round(random.uniform(1.0, 1.9), 1)}

# чтобы записывать статы в файл с именем игрока, создаю функцию, которая будет генерировать имя файла
def file_name(person_name):
    file = ('').join([person_name['name'],'.txt'])
    return file

# функция записи стат в файл
def dict_to_file(file, dictionary):
    with open(file, 'w') as fout:
        for key in dictionary.keys():
            fout.write('%s - %s\n' % (key,dictionary[key]))

# записываю статы в файл
dict_to_file(file_name(player), player)
dict_to_file(file_name(enemy), enemy)

# балуюсь, делаю вид, что сохраняю
print('подождите, пожалуйста, сохраняю файлы')
for i in range(3):
    print('///' * i)
    time.sleep(1)
print('файлы сохранены')

# по условию задачи я должен записать их из файлов => запршиваю, каких игроков загрузить
player_name = input('Введите имя player: ')
enemy_name = input('Введите имя enemy: ')

# функция выгрузки стат из файла
def file_to_dict(file, dictionary):
    with open(file) as file:
        lines = file.readlines()
    for i in lines:
        i = i.split(' - ')
        dictionary.append(i)
    dictionary = dict(dictionary)

# выгружаю статы из файла
dict_to_file(file_name(player), player)
dict_to_file(file_name(enemy), enemy)

# балуюсь, делаю вид, что выгружаю
print('подождите, пожалуйста, выгружаю файлы')
for i in range(3):
    print('///' * i)
    time.sleep(1)
print('данные загружены, статистики игроков')
print(player, '\n', enemy)

# функция нападения
def attack(person1, person2):
    person1['health'] = person1['health'] - person2['damage'] / person1['armor']

# итерация функции, пока у кого то не кончится здоровье
game_round = 0

# из условия не понял, кто бьет первым, поэтому предлагаю выбрать пользователю
player_name = player['name']
enemy_name = enemy['name']
try:
    turn = int(input(f'Кто бьет первым (1 - если {enemy_name} / 2 - если {player_name})?'))
except:
    turn = int(input('Введите число - 1 или 2'))

if turn == 1:
    while player['health'] > 0 and enemy['health'] > 0:
        game_round += 1
        attack(player, enemy)
        print(f'бьет {enemy_name}')
        time.sleep(1)
        print('раунд: {}, player health: {}, enemy health: {}'.format(game_round,
                                                                      player['health'],
                                                                      enemy['health']))
        attack(enemy, player)
        print(f'бьет {player_name}')
        time.sleep(1)
        print('раунд: {}, player health: {}, enemy health: {}'.format(game_round,
                                                                      player['health'],
                                                                      enemy['health']))
        if player['health'] <= 0:
            player['health'] = 0
        elif enemy['health'] <= 0:
            enemy['health'] = 0
elif turn == 0:
    while player['health'] > 0 and enemy['health'] > 0:
        game_round += 1
        attack(enemy, player)
        print(f'бьет {player_name}')
        time.sleep(1)
        print('раунд: {}, player health: {}, enemy health: {}'.format(game_round,
                                                                      player['health'],
                                                                      enemy['health']))
        attack(player, enemy)
        print(f'бьет {enemy_name}')
        time.sleep(1)
        print('раунд: {}, player health: {}, enemy health: {}'.format(game_round,
                                                                      player['health'],
                                                                      enemy['health']))
        if player['health'] <= 0:
            player['health'] = 0
        elif enemy['health'] <= 0:
            enemy['health'] = 0

if enemy['health'] <=0:
    print(f'\nпобедил {player_name}'.upper())
else:
     print(f'\nпобедил {enemy_name}'.upper())

# ПОДКАЖИТЕ, ПЖЛ, ПОЧЕМУ КОГДА БЬЕТ ПЕРВЫМ PLAYER, ИГРА ИДЕТ НОРМАЛЬНО, А КОГДА ENEMY - СРАЗУ ПОБЕЖДАЕТ ENEMY?
# весь вечер ломаю голову, не могу понять ((