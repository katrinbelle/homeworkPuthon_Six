# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения 
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
arithmeticProgression=[]
# arithmeticProgression.append(int(input("Введите первое число-> ")))
# arithmeticProgression.append(int(input("Введите разность чисел> ")))
# arithmeticProgression.append(int(input("Введите количество чисел-> ")))
for i in range(3):
    if i==1: messenge="разность чисел "
    elif i==2: messenge="количество чисел"
    else: messenge="первое число "
    arithmeticProgression.append(int(input(f"Введите {messenge}-> ")))
calculationProgression=arithmeticProgression[0]+(arithmeticProgression[1]-1)*arithmeticProgression[2]
print(f"Арифметическая  прогрессия равна-> {calculationProgression}")