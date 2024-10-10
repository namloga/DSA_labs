import time
import tracemalloc

t_start = time.perf_counter()

fi = open('input.txt', 'r')
fo = open('output.txt', 'w')
tracemalloc.start()

a,b = list(fi.readline().split())

def binaryToArray(bin):
    tmp =[]
    for i in bin:
        tmp.append(i)
    return tmp

def SumBinary(a, b):
    tmp = [0] * (len(a) + 1)
    i = len(a) - 1
    carry = False
    while i >= 0:
        if a[i] == '0' and b[i] == '0':
            if carry:
                tmp[i + 1] = '1'
                carry = False
            else:
                tmp[i + 1] = '0'
        elif (a[i] == '0' and b[i] == '1') or (a[i] == '1' and b[i] == '0'):
            if carry:
                tmp[i + 1] = '0'
                carry = False
            else:
                tmp[i + 1] = '1'
        else:
            if carry:
                tmp[i + 1] = '1'
                carry = True
            else:
                tmp[i + 1] = '0'
                carry = True
        i -= 1
    
    if carry:
        tmp[0] = '1'
    else:
        tmp = tmp[1:]
    return tmp

arr_a = binaryToArray(a)
arr_b = binaryToArray(b)

if len(a) == len(b):    
    s = ''.join(SumBinary(arr_a, arr_b))
    fo.write(f'{s}')
    print("Время 9 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
else:
    fo.write("Длины битов должны быть равны")

fo.close()

# Наихудший случай: Время выполнения в наихудшем случае - O(n)