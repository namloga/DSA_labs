import time
import tracemalloc

t_start = time.perf_counter()

fi = open('input.txt', 'r')

fo = open('output.txt', 'w')
tracemalloc.start()

n = int(fi.readline())
numbers = list(map(int, fi.readline().strip().split()))
flag = True

def selectionSort(a, n):
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    
    return a

for i in numbers:
    if i > 10**9 or i < -10**9:
        flag = False
        break
        
if n < 1 or n > 10**3 or not flag: 
    print("Неверные входные данные")
else:
    numbers = numbers[ :n]
    numbers = selectionSort(numbers, n)
    for i in numbers:
        fo.write(f'{i} ')
    
    print("Время 5 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')

fo.close()

# SelectionSort
# Наихудший случай: Время выполнения в наихудшем случае - O(n^2)
# Средний случай: Время выполнения в наихудшем случае - O(n^2)

# InsertionSort
# Наихудший случай: Время выполнения в наихудшем случае - O(n^2) (массив уже отсортирован в обратном порядке)
# Средний случай: Время выполнения в наихудшем случае - O(n^2) (приходится перемещать элементы при вставке каждого нового элемента)


