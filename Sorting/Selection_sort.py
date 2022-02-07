array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
n = len(array)

''' Selection Sort '''
for i in range(n):
    min_index = i  # 가장 작은 원소의 인덱스
    for j in range(i + 1, n):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # swap

print(array)