fi = open("input.txt")

fo = open("output.txt", "w");

a, b = map(int, fi.read().split());

if (-10**9 <= a <= 10**9) and (-10**9 <= b <= 10**9):
    result = a + b * b;
    fo.write(f'{result}');
else:
    fo.write(f'Неверное входное значение!');
fo.close();
    
