a = input("请输入字符串：")

flag = 0

for i in range(len(a)-1):
    if a[i] == a[i+1]:
        print("yes")
        flag = 1
        break

if flag == 0:
    print("no")