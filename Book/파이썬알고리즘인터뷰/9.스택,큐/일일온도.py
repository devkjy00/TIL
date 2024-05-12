'''
https://leetcode.com/problems/daily-temperatures/

매일 화씨 온도 리스트T를 입력받아서, 더 따듯한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라

:param T: [73, 74, 75, 71, 69, 72, 76, 73]
:return: [1, 1, 4, 2, 1, 1, 0, 0]
'''

def answer(T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last

        stack.append(i)

    return answer
