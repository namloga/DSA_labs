fi = open("input.txt")

fo = open("output.txt", "w");

x = int(fi.read())

def basicLoopFib(n):
    if n == 0: return 0;
    if n == 1 or n == 2:
        return 1;
    first = 1;
    second = 1;
    for i in range (3 , n + 1) :
        second = first + second;
        first = second - first;
    return second;

def solve(n):
    return basicLoopFib(n) % 10;

# print(solve(327305));
fo.write(f"{solve(x)}")

fo.close();