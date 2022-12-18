# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Задайте длину списка: '))
list = []
for i in range(1, n+1):
    list.append(i)
print(list)

from random import randint
 
tmp = []
while len(tmp) < len(list):
    x = randint(0, len(list) - 1)
    if x not in tmp:
        tmp.append(x)
# print(tmp)

new_shuf = []

for i in range(0, len(list)):
    new_shuf.append(list[tmp[i]])
    
print(new_shuf)