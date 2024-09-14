# import time
# t_start = time.perf_counter();

# fi = open("input.txt")

# fo = open("output.txt", "w");

# x = int(fi.read());

# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n+1):
#             c = a + b
#             a = b
#             b = c
#         return b;

# fo.write(f"{fibonacci(x)}");
# print(time.perf_counter() - t_start)