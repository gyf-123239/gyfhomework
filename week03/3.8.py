import random
import time

list = []
a = 100

for i in range(3):
    list.append([])
    for j in range(a):
        list[i].append(random.randint(0, 1000000))
    a *= 10


# 选择排序
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


# 归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


for i in range(len(list)):
    start = time.time()
    selection_sort(list[i])
    selection_time = time.time() - start

    start = time.time()
    merge_sort(list[i])
    merge_time = time.time() - start

    print(selection_time)
    print(merge_time)
