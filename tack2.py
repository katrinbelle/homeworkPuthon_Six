#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
import random
minAndMax=[]
arrayIndex=[]
arrayIndex2=[]
for i in range(2):
    if i==1: messenge="минимальный "
    else: messenge="максимальный"
    minAndMax.append(int(input(f"Введите {messenge} диапозон чисел-> ")))

listRandom=[]
for i in range(20):
    listRandom.append(random.randint(0,20))
print(listRandom)

for i in range(20):
    if listRandom[i]<=minAndMax[0] and listRandom[i]>=minAndMax[1] :
        arrayIndex.append(i)
        arrayIndex2.append(listRandom[i])
print(f"индексы массива между числами {minAndMax[0]} и {minAndMax[1]}-> {arrayIndex}")
