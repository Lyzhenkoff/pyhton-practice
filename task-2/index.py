name = input('Введите свое имя');
goal = input('Введите цель');
persik = 'Персик запомнил вашу цель';

if name == '':
    name = "неизвестный"
elif goal == '':
    persik = 'кажется у вас нету цели'

print('hello', name)
print(persik)