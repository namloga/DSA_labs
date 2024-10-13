import time
import tracemalloc


t_start = time.perf_counter()

fi = open('input.txt', 'r')

fo = open('output.txt', 'w')
tracemalloc.start()

def insertionSort_invate(a, n) :
    l = []
    index = 1
    l.append(index)
    for i in range(1 , n):
        x = a[i]
        pos = i - 1;
        while pos >= 0 and a[pos] > x :
            a[pos + 1] = a[pos]
            pos -= 1
        a[pos + 1] = x
        index = pos + 2
        l.append(index)
    return a, l

n = int(fi.readline())
numbers = list(map(int, fi.readline().strip().split()))
flag = True

for i in numbers:
    if i > 10**9 or i < -10**9:
        flag = False
        break
    
if flag:
    numbers = numbers[ :n]
    numbers, indexes = insertionSort_invate(numbers, n)
        
    for i in indexes:
        fo.write(f'{i} ')
        
    fo.write('\n')
        
    for i in numbers:
        fo.write(f'{i} ')
    print("Время 2 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
else:
    print("Неверные входные данные")

fo.close()
