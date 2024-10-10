import time
import tracemalloc

t_start = time.perf_counter()

fi = open('input.txt', 'r')

fo = open('output.txt', 'w')
tracemalloc.start()

n = int(fi.readline())
numbers = list(map(int, fi.readline().split()))
flag = True

def bubbleSort(a, n):
    for i in range(n -1, 0, -1):
        for j in range(1, i + 1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    
    return a

for i in numbers:
    if i > 10**9 or i < -10**9:
        flag = False
        break

if n < 1 or n > 10**3 or not flag: 
    print("Неверные входные данные")
else:
    numbers = numbers[ :n]
    numbers = bubbleSort(numbers, n)
    for i in numbers:
        fo.write(f'{i} ')
    
    print("Время 6 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')

fo.close()

# BubbleSort
# Наихудший случай: Время выполнения в наихудшем случае - O(n^2)
# Средний случай: Время выполнения в наихудшем случае - O(n^2)
