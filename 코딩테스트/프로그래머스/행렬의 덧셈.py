# 같은행 같은 열 더하기


def solution(arr1, arr2):
    answer = []
    row = 0
    for A, B in zip(arr1, arr2):
        answer.append([])
        for x, y in zip(A, B):
            answer[row].append(x + y)
        row += 1

    return answer


# 더 간단한 풀이 원리는 같다, []안에 for 문 정의해서 간단하게 차원분리
# 다 짜고 나서 항상 리팩토링을 하자
# answer = [[c + d for c, d in zip(a, b)]
#                   for a, b in zip(A,B)]


# numpy를 이용해서 연산
import numpy as np

a = np.array([[1, 2], [2, 3]])
b = np.array([[3, 4], [5, 6]])
answer = a + b
answer.tolist()
