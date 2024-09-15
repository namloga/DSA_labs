import time
t_start = time.perf_counter();

fi = open("input.txt")

fo = open("output.txt", "w");

x = int(fi.read());

def fibonacci(n, cache = [0, 1, 1]):
    if n < len(cache):
        return cache[n]
    
    cache.append(fibonacci(n - 1, cache) + fibonacci(n - 2, cache))
    return cache[n]

fo.write(f"{fibonacci(x)}");

print("Время 2 задания:", time.perf_counter() - t_start)

fo.close()