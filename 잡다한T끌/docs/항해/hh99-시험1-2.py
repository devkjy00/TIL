'''
https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

기능의 개발진도 0~100와 개발속도가 주어진다
기능은 순서대로 배포되서 개발이 완료되더라도 앞의 기능이 배포될때 뒤에기능도 배포된다

:param progresses: [93, 30, 55],
:param speeds: [1, 30, 5]
:return: [2, 1]
'''
import collections

def solution(progresses, speeds):
    '''
    첫 기능이 100이 되면 배포 ->  스택으로 구현
    기능이 100이 될때 까지 속도를 더한다
    100 이상인 모든 기능을 꺼낸다
    '''
    progresses = progresses[::-1]
    speeds = speeds[::-1]
    table = collections.defaultdict(int)
    count = 0

    while progresses:
        if progresses[-1] >= 100:
            progresses.pop()
            speeds.pop()
            table[count] += 1
        else:
            count += 1
            for i, num in enumerate(speeds):
                progresses[i] += num

            # print("진도: ", progresses)
    # print(table)
    return list(table.values())



print(solution([2, 1], [1, 1]))