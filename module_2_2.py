first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second != third or second == third != first or first == third != second:
    print(2)
elif first and second != third:
    print(0)
elif first and second == third:
    print(3)