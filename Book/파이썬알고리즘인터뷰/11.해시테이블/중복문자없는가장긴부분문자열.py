'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/

중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라

:param s: "pwwkew"
:return: 3
'''
import collections


def solution(s):
    '''
    필요한 알고리즘 : 중복 값인지 검사->사전, 중복되지 않은 문자열 저장(더 긴 값으로 업데이트)
    '''
    str = []
    length = []
    for ch in s:
        if ch in str:
            length.append(len(str))
            str = str[str.index(ch)+1:]
        str.append(ch)

    length.append(len(str))
    return max(length)

print(solution(" "))


def answer(s):
    '''
    index함수를 사용하지 않고 사전에 직접 인덱스 값을 저장해서 중복되면 포인터를 옮겨줬다
    -> 중복된 값의 위치를 덮어쓰면서 자연스럽게 위치 이동
    '''
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1

        else:
            max_length = max(max_length, index - start + 1)

        used[char] = index

    return max_length