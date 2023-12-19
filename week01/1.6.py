w = int(input("请输入w："))
x = int(input("请输入x："))
y = int(input("请输入y："))
z = int(input("请输入z："))

if w > x:
    w, x = x, w
if w > y:
    w, y = y, w
if w > z:
    w, z = z, w
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y

print(w, x, y, z)