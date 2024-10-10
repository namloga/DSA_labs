import time
import tracemalloc


t_start = time.perf_counter()

fi = open('input.txt', 'r')

fo = open('output.txt', 'w')
tracemalloc.start()

n = int(fi.readline())
numbers = list(map(float, fi.readline().split()))
flag = True

def checkValue(x):
    s = str(x)
    index_Decimal = s.find('.')
    l_Decimal = len(s[index_Decimal + 1:])
    if l_Decimal <= 2:
        return True
    else: return False

def bubbleSort(a, n):
    for i in range(n -1, 0, -1):
        for j in range(1, i + 1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    
    return a

def Search(a, n, x) :
    for i in range(n):
        if a[i] == x:
            return i
        
def solve(a, tmp, n):
    numbers_id = []
    value_max = a[n - 1]
    value_min = a[0]
    value_medium = a[n // 2]
    
    numbers_id.append(Search(tmp, n, value_min))
    numbers_id.append(Search(tmp, n, value_medium))
    numbers_id.append(Search(tmp, n, value_max))
        
    return numbers_id

for i in numbers:
    if i > 10**6 or i < -10**6 or checkValue(i) == False:
        flag = False
        break

if flag:
    if n >= 3 and n < 1000 and n % 2 != 0:
        numbers = numbers[ :n]
        tmp = numbers[:]
        numbers = bubbleSort(numbers, n)
        answer = solve(numbers, tmp, n)
        for i in answer:
            fo.write(f'{i + 1} ')
        print("Время 7 задания:", time.perf_counter() - t_start)
        print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
    else:
        print("Неверные входные данные")
else:
    print("Неверные входные данные")
    
fo.close()

