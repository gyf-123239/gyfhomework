accuracy = 8


def dtb(num):
    integer = int(num)
    flo = num - integer
    tmp = flo

    itb = bin(integer)
    ftb = ""

    for i in range(accuracy):
        ftb += str(int(tmp * 2))
        tmp = tmp * 2 - int(tmp * 2)
    return itb + '.' + ftb


num = float(input("请输入一个小数："))

print(dtb(num))
