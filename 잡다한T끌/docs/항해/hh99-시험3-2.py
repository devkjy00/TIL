'''
https://programmers.co.kr/learn/courses/30/lessons/43238


'''

def solution(n, times):
    '''
    심사관이 일한 시간이 같아야 한다
    가장 빠른 심사관을 기준으로
    0 ~ n 명의 사람들을 이진 탐색해서 진행된 시간만큼
    다른 심사관이 처리할 수 있는 수를 찾는다
    전체 수보다 많으면 왼쪽 적으면 오른쪽으로 가서 다시 이진탐색
    '''
    left, right = 1, n
    table = [-1] * n
    times.sort()

    while left <= right:
        mid = (left + right) // 2
        given_time = (mid * times[-1])
        result = mid

        for time in times[:-1]:
            result += given_time // time

        if result > n:
            table[mid] = given_time
            if mid < n and table[mid-1] == 0:
                return given_time
            right = mid - 1

        elif result < n:
            table[mid] = 0

            if mid > 0 and table[mid+1] > 0:
                return table[mid+1]
            left = mid + 1
        else:
            return given_time

        print()

print(solution(8, [5, 7, 12]))
