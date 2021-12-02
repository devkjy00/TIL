# 리스트를 슬라이싱(i:j)해서 k번째 수 구하기

# [i,j,k]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
array = [1, 5, 2, 6, 3, 7, 4]

for i, j, k in commands:
    print(sorted(array[i - 1 : j])[k - 1])
