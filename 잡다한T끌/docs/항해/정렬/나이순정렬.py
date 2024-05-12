'''
https://www.acmicpc.net/problem/10814

- 입력
3
21 Junkyu
21 Dohyun
20 Sunyoung
'''





def solution(customer):
    result = [(int(element[0]), idx, element[1]) for idx, element in enumerate(customer)]
    result.sort()
    print(result)
    # return [[element[0], element[2]] for element in result]

    for element in result:
        print(element[0], element[2])

# solution([input().split() for _ in range(int(input()))])
print(solution([['21', 'Junkyu'], ['21', 'Dohyun'], ['20', 'Sunyoung']]))




