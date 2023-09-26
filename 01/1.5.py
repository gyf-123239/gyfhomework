x = int(input("请输入x："))
y = int(input("请输入y："))
z = int(input("请输入z："))

if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print(x, y, z)
