import time

t_start = time.perf_counter();
fi = open("input.txt")

fo = open("output.txt", "w");

x = int(fi.read());

def loopFib (n):
    if n < 0: return;
    if n == 0: return 0;
    if n == 1 or n == 2:
        return 1;
    first = 1;
    second = 1;
    for i in range (3 , n+1) :
        second = first + second;
        first = second - first;
    return second;

def solve(n):
    return loopFib(n) % 10;

fo.write(str(loopFib(x) % 10))

print("Время 3 задания:", time.perf_counter() - t_start);
fo.close();