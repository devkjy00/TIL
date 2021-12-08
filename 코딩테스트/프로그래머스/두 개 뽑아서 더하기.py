import itertools


def solution(numbers):
    subset = itertools.permutations(numbers, 2)
    answer = {i[0] + i[1] for i in subset}
    return sorted(list(answer))


# 테스트
numbers = [2, 1, 3, 4, 1]
result = [2, 3, 4, 5, 6, 7]

assert result == solution(numbers)

# itertools.permutations(배열, 개수)
# 입력된 개수로 구성된 부분집합튜플을 반환
# 같은 원소를 위치만 바꾼 집합도 있기 때문에 연산시 주의
