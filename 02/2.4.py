c = int(input("请输入需要开方的值:"))
h = 0.0001
g = 0

for i in range(0, c + 1):
    if i ** 2 <= c <= (i + 1) ** 2:
        g = i

while abs(g ** 2 - c) > h:
    g += h

print(g)
