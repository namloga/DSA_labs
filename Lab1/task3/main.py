import time
import tracemalloc


t_start = time.perf_counter()

fi = open('input.txt', 'r')

fo = open('output.txt', 'w')
tracemalloc.start()

def insertionSort_decrease(a, n):
    for i in range(1, n):
        x = a[i]
        pos = i - 1
        while pos >= 0 and x > a[pos]:
            a[pos + 1] = a[pos]
            pos -= 1
        a[pos + 1] = x
    return a

def insertionSort_decrease_recursive(a, n):
    if n > 1:
        insertionSort_decrease_recursive(a, n - 1)
    
    x = a[n - 1]  
    pos = n - 2   
    while pos >= 0 and x > a[pos]:
        a[pos + 1] = a[pos]
        pos -= 1
    a[pos + 1] = x

n = int(fi.readline())
numbers = list(map(int, fi.readline().strip().split()))
flag = True

for i in numbers:
        if i > 10**9 or i < -10**9:
            flag = False
            break
        
if n < 1 or n > 10**3 or not flag: 
    print("Неверные входные данные")
else:
    numbers = numbers[ :n]
    insertionSort_decrease(numbers, n)
    # numbers = insertionSort_decrease(numbers, n)
    for i in numbers:
        fo.write(f'{i} ')
    
    print("Время 3 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')

fo.close()
