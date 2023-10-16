def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return b


num1 = int(input("请输入第一个正整数："))
num2 = int(input("请输入第二个正整数："))

ans = gcd(num1, num2)

print(ans)
