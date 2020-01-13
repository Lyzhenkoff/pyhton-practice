a = int(input('Введите число '))
b = int(input('Введите число '))
spo = input('Введите операцию(+,-,*,/) ')

if spo == '+':
    c = a+b
elif spo == '-':
    c = a-b
elif spo == '*':
    c = a*b
elif spo == '/':
    c = a/b

print(c)