'''
https://leetcode.com/problems/longest-palindromic-substring/

가장 긴 팬린드롬 부분 문자열을 출력하라
palindromic : 역순으로 읽어도 같은 말이 되는 말

:param input: s = "babad"
:return: "bab" or "aba"
'''

def solution(s):
    '''
    시간 초과를 해결하지 못했다...
    '''
    s_len = len(s)
    if s_len <= 1:
        return s
    palin_list = []

    for i in range(2, s_len+1):
        for j in range(0, s_len):
            str = s[j:j+i]
            if str == str[::-1]:
                print(str)
                palin_list.append(str)

    return sorted(palin_list, key=lambda x:len(x))[-1]

def answer(s):
    '''
    1. 짝수의 경우를 위해 2칸, 홀수의 경우를 위해 3칸 이 팰린드롬인지 비교하는 두 포인터로 검사
        - 고려해야할 경우의 수만 찾아서 검사하도록 한다
    2. 팰린드롬을 찾으면 그자리에서 양쪽으로 2칸씩 확장해서 가장 긴 팰린드롬을 찾는다
        - 모든 경우를 순서대로가 아니라 적합한 경우 그자리에서 멈춰서 값을 찾는다

    - max()에도 key를 적용할 수 있다
    '''
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(0, len(s) - 1):

        result = max(result,
                     expand(i, i+1),
                     expand(i, i+2),
                     key=len)

    return result

print(answer("babad"))