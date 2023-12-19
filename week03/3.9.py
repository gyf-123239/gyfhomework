# 举例
A = [8, 6, 3, 2, 1]
B = []

for i in range(len(A)):
    left = 1
    right = 1
    for j in range(i):
        left *= A[j]
    for k in range(i + 1, len(A)):
        right *= A[k]
    B.append(left * right)

print(B)
