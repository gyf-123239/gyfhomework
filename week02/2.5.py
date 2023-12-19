c = int(input("请输入需要开方的值:"))
h = 0.0000001
g = c / 2

while abs(g ** 2 - c) > h:
    g = (g + c / g) / 2

print(g)
