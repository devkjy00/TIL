def find_cloth(num, lost, reserve):
    for i in [0, -1]:
        if num + i in reserve:

            reserve.remove(num + i)
            return True

    if num + 1 in reserve:
        if num + 1 in lost:
            return False
        else:
            reserve.remove(num + 1)
            return True
    return False


n = 10  # 학생수
lost = [1, 2, 3, 4, 5, 6]
reserve = [7, 8, 9]
answer = 0


for i in range(1, n + 1):
    if i in lost:
        if find_cloth(i, lost, reserve):
            answer += 1
            continue
        else:
            continue
    answer += 1

print(answer)

#
