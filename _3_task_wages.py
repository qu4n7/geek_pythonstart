# пишет ввод в файл
def data_to_file(file):
    dct = []
    print('оставь поля пустыми, чтобы закончить')
    with open(file, 'w') as f:
        while True:
            sname = input('фамилия?')
            wage = input('зп?')
            if sname:
                f.write(f'{sname} : {float(wage)}\n')
            else: 
                break

# читает файл
def read_txt(file):
    salary = []
    with open(file) as f:
        lines = f.readlines()
    for i in lines:
        i = i.split(' : ')
        salary.append(i)
    return dict(salary)

# выводит статы
def my_stat(dct):
    print('меньше 20:')
    for sname, wage in dct.items():
        if float(wage) < 20000:
            print(sname)
    print(f'\nсредняя: {sum([float(x) for x in dct.values()]) / len(dct)}')

# пускаем 
data_to_file('salary.txt')
my_stat(read_txt('salary.txt'))