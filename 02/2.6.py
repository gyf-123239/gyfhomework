c = int(input("请输入需要开方的值:"))
h = 0.0000001
g1 = c
g2 = c / 2
g3 = c / 4

while abs(g1 ** 2 - c) > h:
    g1 = (g1 + c / g1) / 2
    g2 = (g2 + c / g2) / 2
    g3 = (g3 + c / g3) / 2

print(g1, g2, g3)
# 对结果会有影响，但相差不大
