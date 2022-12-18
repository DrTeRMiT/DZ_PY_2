# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('введите число: '))
n2 = n* -1

x = int(input('Введите номер первой позиции: '))
y = int(input('Введите номер второй позиции: '))

list = []
for i in range(n2, n + 1):
    list.append(i)

with open('file.txt', 'w') as f:
    f.write('\n')
    f.write(f'{x}' + '\n')
    f.write(f'{y}' + '\n')

tmp =[]
path = 'file.txt'
data = open(path, 'r')
for line in data:
    tmp = data.readlines()
data.close()

print(tmp)

a = int(tmp[0])
b = int(tmp[1])
 
sum = (list[a-1])*(list[b-1])

print(f"x {n}:  {list}")
print(sum)