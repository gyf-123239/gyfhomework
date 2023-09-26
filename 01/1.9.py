list = [1, 2, 3, 4, 5]

list_2 = []

i = 4

for a in range(5):
    list_2.append(list[i])
    i = i - 1

j = 4

while j >= 0:
    list_2.append(list[j])
    j = j - 1

print(list_2)