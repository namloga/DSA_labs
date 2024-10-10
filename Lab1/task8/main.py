import time
import tracemalloc


t_start = time.perf_counter()

fi = open('input.txt', 'r')

fo = open('output.txt', 'w')

n = int(fi.readline())
numbers = list(map(int, fi.readline().strip().split()))
flag = True
tracemalloc.start()

def selectionSort(a, n):
    pairs = []
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        if i != min_index:
            pairs.append((i + 1, min_index + 1))
    return a, pairs;

for i in numbers:
    if i > 10**9 or i < -10**9:
        flag = False
        break

if n < 3 or n > 5000 or not flag: 
    print("Неверные входные данные")
else:
    numbers = numbers[ :n]
    numbers, pairs = selectionSort(numbers, n)
    for i, j in pairs:
        fo.write(f'Swap elements at indices {i} and {j} \n')
    fo.write(f'No more swaps needed.')
    
    print("Время 8 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')

fo.close()
