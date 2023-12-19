import re


def idcard(id):
    pattern = r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[1-2]\d|3[0-1])\d{3}(\d|X|x)$'

    # 使用正则表达式匹配身份证号
    if re.match(pattern, id):
        return True
    else:
        return False


id = input("请输入身份证号：")

print(idcard(id))
