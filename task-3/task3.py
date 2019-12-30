a = input('Введите числа через запятую ');

splt = a.split(',');
ints = map(int, splt);
lst = list(ints)

print(lst);