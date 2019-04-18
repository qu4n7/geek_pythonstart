import random, sys

class Barrel:
    # создается перечень номеров бочонков, перемешивается
    # выводится номер бочонка и кол-во оставшихся
    def f(self):
        lst = [x for x in range(1, self.amount + 1)]
        random.shuffle(lst)
        for i, y in enumerate(lst):
            print('{:_^30}'.format('_'))
            print('номер бочнка: {} (осталось {})'.format(y, self.amount - (i + 1)))
            yield y

    def __init__(self, amount):
        self.amount = amount
        self.gen = self.f()

class Game:
    # создается карточка
    def __set_card(self):
        # заводится переменную типа сет
        num = set()
        # генерируется случайные числа
        while len(num) < self.all_row * 5:
            num.add(random.randint(1, 91))
        # загоняетя в тип лист
        cards = list(num)
        random.shuffle(cards)

        while len(cards) % self.all_row != 0:
            cards.append('None')
        self.all_row = int(len(cards) / self.all_row)
        cards = [cards[i: i + self.all_row] for i in range(0, len(cards), self.all_row)]

        # разрезаю первые 3 строчки на игрока, следующие 3 на компьютер
        for i in range(len(cards)):
            cards[i].sort()
        self.card_player = cards[:3]
        self.card_enemy = cards[3:]

    def __init__(self, amount_card):
        row = 3
        self.all_row = row * amount_card
        self.__set_card()

    # визуализирую карточки, при этом места заполнения фиксированы
    # как сделать ячейки заполнения рандомными пока не понял
    def vslz(self, card_player):
        print('{:-^25}'.format(self.name))
        print('{0[0]:>2} {0[1]:<5} {0[2]:<10} {0[3]} {0[4]} '.format(card_player[0]))
        print('{0[0]:>2} {0[1]:<8} {0[2]:<4} {0[3]:<4} {0[4]} '.format(card_player[1]))
        print('{0[0]} {0[1]:<2} {0[2]:<8} {0[3]:<5} {0[4]} '.format(card_player[2]))
        print('{:-^25}'.format('|'))

    # поиск номера, выбор победителя
    def search(self, card_player, num_barrel):
        for i, n in enumerate(card_player):
            if num_barrel in n:
                card_player[i][n.index(num_barrel)] = '-'
                self.score += 1
                if self.score == 15:
                    print('победил {}'.format(self.name))
                    sys.exit(1)
                return True
        return False


# завожу класс игрока с общими свойствами для меня и компа - имя, счет
class Player(Game):
    def __init__(self, name):
        self.name = name
        self.score = 0


# функция проведения игры
def main():
    game = Game(2)
    barrel = Barrel(90)
    player = Player('моя карточка')
    enemy = Player('карточка компьютера')

    while True:
        num_barrel = next(barrel.gen)
        # показываю карточки
        player.vslz(game.card_player)
        enemy.vslz(game.card_enemy)

        # запрашиваю действие
        inp_user = input('Зачеркнуть цифру? (y/n)')
        # вызываю сопоставление бочонка и номеров в карте
        if inp_user == 'y':
            if player.search(game.card_player, num_barrel):
                continue
            else:
                print('вы проиграли')
                sys.exit('выпавший номер бочонка отсутствовал у вас')
        if inp_user == 'n':
            if player.search(game.card_player, num_barrel):
                print('вы проиграли')
                sys.exit('вы не зачеркнули выпавший номер бочонка')
            elif enemy.search(game.card_enemy, num_barrel):
                continue
        # проверка формата ввода
        if inp_user != 'n' and inp_user != 'y':
            print('некорректный формат ввода, введите y or n')
            сontinue


if __name__ == '__main__':
    main()