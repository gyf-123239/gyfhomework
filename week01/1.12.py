a = int(input("请输入数字："))

x = 0.0000001
low = 0
high = a
ans = (high + low) / 2

while (ans * ans * ans > (a + x)) or (ans * ans * ans < (a - x)):
    if ans * ans * ans > a + x:
        high = (high + low) / 2
        ans = (high + low) / 2
    if ans * ans * ans < a - x:
        low = (high + low) / 2
        ans = (high + low) / 2

print(ans)
