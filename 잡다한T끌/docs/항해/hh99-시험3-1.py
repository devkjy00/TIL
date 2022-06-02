'''
https://programmers.co.kr/learn/courses/30/lessons/43105

:param triangle: [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
:return: 30
'''





def solution(triangle):
    '''
    상위 계층의 두 수중 큰 수를 아래 수에 더한다
    '''

    layer = 1

    while layer < len(triangle):
        for idx, num in enumerate(triangle[layer]):
            if idx == 0:
                triangle[layer][idx] += triangle[layer-1][idx]
            elif idx == len(triangle[layer])-1:
                triangle[layer][idx] += triangle[layer-1][idx-1]
            else:
                triangle[layer][idx] += max(
                    triangle[layer-1][idx-1], triangle[layer-1][idx])
        layer += 1

    print(max(triangle[-1]))


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])



def solution_prog(triangle):
    '''
    아래부터 올라가서 [0][0]이 최댓값이 되도록 했다
    -> if 문으로 가지치기 할 필요 없음
    -> 규칙의 좋은 부분만 취해서 풀이..
    '''

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer