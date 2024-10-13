import time
import tracemalloc

t_start = time.perf_counter()

fi = open('input.txt', 'r')
fo = open('output.txt', 'w')
tracemalloc.start()

n = int(fi.readline())
s = fi.readline()
flag = True

for i in s:
    if not (i.isalpha() and i.upper() != i):
        flag = False
        break

def InsertionSort(s, n):
    for i in range(1, n):
        x = s[i]
        pos = i - 1
        while pos >= 0 and s[pos] > x:
            s[pos + 1] = s[pos]
            pos -= 1
        s[pos + 1] = x
    return s

def count_Chars(s, n):
    list_count = []
    s = InsertionSort(s, len(s))
    count_odd_char = 0
    count_one_char = 0
    count_odd_max = 0
    i = 0
    while i < n: 
        count = 1
        j = i + 1
        while j < n and s[i] == s[j]:
            count += 1
            j += 1
        if count % 2 != 0 and count >= 3:
            count_odd_char += 1
            count_odd_max = count
        if count == 1:
            count_one_char += 1
        list_count.append((s[i], count)) 
        i = j
    return list_count, count_odd_char, count_one_char, count_odd_max
    

def palindrome(s, n):
    tmp, count_odd, count_1, count_odd_max = count_Chars(s, n)
    count_palindrome_mid = 1
    s_palindrome_left = ""
    s_palindrome_right = ""
    s_palindrome_mid = ""
    result = ""
    for i,j in tmp:
        if j % 2 == 0:
            while j != 0:
                s_palindrome_left += i
                s_palindrome_right += i
                j -= 2
        else:
            if count_odd >= 1:
                if j >= 3:
                    x = j
                    while x != 1:
                        s_palindrome_left += i
                        s_palindrome_right += i
                        x -= 2
                    if j == count_odd_max:
                        if count_palindrome_mid > 0:
                            s_palindrome_mid = i
                            count_palindrome_mid -= 1
            else:
                if count_1 == 1:
                    s_palindrome_mid = i
                else:
                    if count_palindrome_mid > 0:
                        s_palindrome_mid = i
                        count_palindrome_mid -= 1
    result = s_palindrome_left + s_palindrome_mid + s_palindrome_right[::-1]       
    return result

arr_string = [i for i in s]
flag = True


for i in s:
    if not (i.isalpha() and i.upper() == i):
        flag = False
        break
if (n < 1 or n > 100000) or not flag:
    print("Неверные входные данные")
else:
    fo.write(f'{palindrome(arr_string, len(arr_string))}')
    
    print("Время 10 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
fo.close()
