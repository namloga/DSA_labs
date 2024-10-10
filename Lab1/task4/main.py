import time
import tracemalloc


t_start = time.perf_counter()

fi = open('input.txt', 'r')

fo = open('output.txt', 'w')
tracemalloc.start()

def Search(a, n):
    count = 0
    l = []
    for i in range(len(a)):
        if a[i] == n:
            count += 1;
            l.append(i)
    if count > 1:
        return count, l
    elif count == 0:
        l.append(-1)
    return l;

numbers = list(map(int, fi.readline().split()))
k = int(fi.readline())
flag = True

if k > 10**3 or k < -10**3:
    print("Неверные входные данные")
else:
    for i in numbers:
        if i > 10**3 or i < -10**3:
            flag = False
            break
    
    if flag:
        result = Search(numbers, k)

        if len(result) > 1:
            count, listOfIndex = Search(numbers, k)
            fo.write(f"{count} ")
            for i in range(0, len(listOfIndex)):
                if i == len(listOfIndex) - 1:
                    fo.write(f"{listOfIndex[i]}")
                else: 
                    fo.write(f'{listOfIndex[i]},')
        else:
            fo.write(f"{result[0]}")
    else:
        print("Неверные входные данные")
        
    print("Время 4 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')

fo.close()
