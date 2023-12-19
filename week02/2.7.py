c = int(input("请输入需要开方的值:"))
h = 0.0000001
g = c / 2

while abs(g ** 3 - c) > h:
    g = (2 * g + c / (g * g)) / 3

print(g)
