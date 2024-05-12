'''
https://leetcode.com/problems/valid-parentheses/

괄호로 된 입력값이 올바른지 판별하라

:param s: "()[]{}"
:return: true
'''

def answer(s):
    '''
    in 연산자로 사전의 키값 중에 없으면 스택에 넣도록 구현

    '''
    bracket = {")": "(",
              "]": "[",
              "}": "{"}
    stack = []

    for ch in s:
        if ch not in bracket:
            stack.append(ch)
        elif not stack or bracket[ch] != stack.pop():
            return False

    return len(stack) == 0

print(answer("()[]{}"))

