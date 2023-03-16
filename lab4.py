def z1():
    spisok = [1, 3, 5, 7, 9]
    number = input('Введите число: ')
    if int(number) in spisok:
        print('Поздравляю, Вы угадали число!')
    else:
        print('Нет такого числа!')

def z2():
    k = 0
    spisok = [1, 2, 3, 4, 5, 2]
    for i in spisok:
        if spisok.count(i) > 1 and i != k:
            print(i)
            k = i

def z3():
    week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    weekends = int(input('Количество выходных: '))
    print('Ваши выходные дни: ', *week[len(week)-weekends:])
    print('Ваши рабочие дни: ', *week[:-weekends])

def z4():
    import random
    a = ['Коровашев', 'Рубцова', 'Иванов', 'Ольховский', 'Бабушкин']
    b = ['Черненко', 'Ирматов', 'Голяев', 'Нуратдинов', 'Насулина']
    num1 = list(range(5))
    random.shuffle(num1)
    num2 = list(range(5))
    random.shuffle(num2)
    sport = [a[i] for i in num1[:3]] + [b[i] for i in num2[:3]]
    print('\n Первый список: ', *a, '\n Второй список: ', *b, '\n Спортивная команда: ', *sport)
    print(' Длина кортежа: ', len(sport))
    sport = sorted(sport)
    print(' Отсортированный кортеж: ', *sport)
    if 'Иванов' in sport:
        print(' В команде есть Иванов!')
        print(' Сколько раз встречается фамилия: ', sport.count('Иванов'))
    else:
        print(' В команде нет Иванова!')

z1()
z2()
z3()
z4()