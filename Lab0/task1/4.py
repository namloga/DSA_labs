fi = open("input.txt")

fo = open("output.txt", "w");

s = fi.read().split();

for i in range (0, len(s)):
    s[i] = int(s[i]);

a = s[0]
b = s[1];

result = a + b * b;
    
fo.write(f'{result}');

fo.close();