score = float(input("请输入考试成绩（百分制）："))

if score >= 90:
    grade = "优秀"
elif score >= 75:
    grade = "良好"
elif score >= 60:
    grade = "合格"
else:
    grade = "不合格"

print(grade)
