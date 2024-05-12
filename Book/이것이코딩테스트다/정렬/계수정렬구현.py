array = [3, 7, 9, 8, 3, 5, 7, 5, 2, 5, 8, 4, 3]

count = [0] * (max(array) + 1)

for i in array:
    count[i] += 1

for num, i in enumerate(count):
    print(num, i, end=' ')