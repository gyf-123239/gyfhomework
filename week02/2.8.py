import time

# 法一
start = time.perf_counter()

import random

s = 1e4
n = 0

for i in range(int(s)):
    x = random.random()
    y = random.random()
    d = (x - 0.5) ** 2 + (y - 0.5) ** 2
    if d <= 0.5 ** 2:
        n += 1

PI_1 = 4 * n / s

print(PI_1)

end = time.perf_counter()
print(str(end - start))

# 法二
start = time.perf_counter()

PI_2 = 0
n = 1e4

for i in range(int(n)):
    PI_2 += (1 / pow(16, i)) * (4 / (8 * i + 1) - 2 / (8 * i + 4) - 1 / (8 * i + 5) - 1 / (8 * i + 6))

print(PI_2)

end = time.perf_counter()
print(str(end - start))

# 法三
start = time.perf_counter()

PI_3 = 0
n = 1e4

for i in range(int(n)):
    PI_3 += (-1) ** i / (2 * i + 1) * 4

print(PI_3)

end = time.perf_counter()
print(str(end - start))
