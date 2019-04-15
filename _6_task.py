print('easy'.upper())
# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
class TownCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = is_police
    def go(self):
        print('машина поехала')
    def stop(self):
        print('машина остановилась')
    def turn(self, direction):
        print('машина повернула', direction)

class SportCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('машина поехала')
    def stop(self):
        print('машина остановилась')
    def turn(self, direction):
        print('машина повернула', direction)

class WorkCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('машина поехала')
    def stop(self):
        print('машина остановилась')
    def turn(self, direction):
        print('машина повернула', direction)

class PoliceCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('машина поехала')
    def stop(self):
        print('машина остановилась')
    def turn(self, direction):
        print('машина повернула', direction)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('машина поехала')
    def stop(self):
        print('машина остановилась')
    def turn(self, direction):
        print('машина повернула', direction)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

print('normal'.upper())
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import time
import random


# создаю общий класс
class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    # метод для подсчета урона с учетом брони
    def damage_q(person1, person2):
        damage_qu = person2.damage / person1.armor
        print('урон составил {:.0f}'.format(damage_qu))

    # метод для атаки
    def attack(person1, person2):
        person1.health = person1.health - person2.damage / person1.armor
        print('у игрока {} осталось {:.0f} здоровья'.format(person1.name, person1.health))


# наследуясь от Person создаю
class Player:
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)

    def damage_q(person1, person2):
        damage_qu = person2.damage / person1.armor

    def attack(person1, person2):
        Person.attack(person1, person2)


class Enemy:
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)

    def damage_q(person1, person2):
        damage_qu = person2.damage / person1.armor

    def attack(person1, person2):
        Person.attack(person1, person2)


# генерация статов
player = Player(input('Введите имя player: '), random.randrange(50, 200), random.randrange(5, 51),
                round(random.uniform(1.0, 1.9), 1))
enemy = Enemy(input('Введите имя enemy: '), random.randrange(50, 200), random.randrange(5, 51),
              round(random.uniform(1.0, 1.9), 1))
print(f'\nу игрока {player.name} следующие параметры:\nздоровье {player.health}\nурон {player.damage}\n'
      f'защита {player.armor}')
print(f'\nу игрока {enemy.name} следующие параметры:\nздоровье {enemy.health}\nурон {enemy.damage}\n'
      f'защита {enemy.armor}')
# как описать цикл через класс и вызывать его я не совсем, точнее совсем, не придумал
game_round = 0
print('\nда начнется бой!')
time.sleep(3)
while player.health > 0 and enemy.health > 0:
    game_round += 1
    player.attack(enemy)
    print(f'бьет {enemy.name}')
    time.sleep(1)

    enemy.attack(player)
    print(f'бьет {player.name}')
    time.sleep(1)

# вывод результата
if enemy.health <= 0 and player.health <= 0:
    print('игроки самоубились'.upper())
elif enemy.health <= 0:
    print(f'\nпобедил {player.name}'.upper())
else:
    print(f'\nпобедил {enemy.name}'.upper())