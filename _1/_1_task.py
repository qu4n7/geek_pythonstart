# Python-1-lesson1-easy
# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

var1, var2 = 10, 3
print(f'остаток от деления 10 на 3 равено {var1%var2} \nтеперь попробуйте Вы.')
var1 = int(input('Введите первое число:'))
var2 = int(input('Введите второе число:'))
print(f'остаток от деления: {var1%var2}')

print('\n')
# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

number = int(input('Введите число:'))
number += 2
print(f'Сумма Вашего числа и 2 равна: {number}')

print('\n')
# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введите Ваш возраст:'))
if age < 18:
    print('Извините, пользование данным ресурсом только с 18 лет')
elif age >= 18:
    print('Доступ разрешен')

print('\n')
# Python-1-lesson1-normal

# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степерь 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заного.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

number = int(input('Введите число от 1 до 9:'))
while number < 1 or number > 9:
    print('Вы ввели некорректное число, число должны быть в диапозоне от 1 до 9.')
    number = int(input('Пожалуйста, введите корректное число - от 1 до 9:'))
print(f'квадрат Вашего числа равен: {number**2}')

print('\n')
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

input1 = input('Введите значение первой переменной:')
input2 = input('Введите значение второй переменной:')
input1, input2 = input2, input1
print(f'значение первой переменной:{input1}, значение второй переменной:{input2}')

print('\n')
# Python-1-lesson1-hard

# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

name = input('Введите Ваше имя:')
surname = input('Введите Вашу фамилию:')
age = int(input('Введите Ваш возраст:'))
weight = int(input('Введите Ваш вес:'))

if age <= 40:
    if weight >= 50 and weight <= 120:
        print(f'{name} {surname}, возраст: {age}, вес: {weight} - хорошее состояние')
    else:
        print(f'{name} {surname}, возраст: {age}, вес: {weight} - следует заняться собой')
else:
    if weight >= 50 and weight <= 120:
        print(f'{name} {surname}, возраст: {age}, вес: {weight} - хорошее состояние, но регулярно наблюдайтесь у врача')
    else:
        print(f'{name} {surname}, возраст: {age}, вес: {weight} - следует обратится к врачу!')