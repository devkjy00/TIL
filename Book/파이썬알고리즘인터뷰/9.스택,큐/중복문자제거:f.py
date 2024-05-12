'''
https://leetcode.com/problems/remove-duplicate-letters/

중복된 문자를 제외하고 사전식 순서(Lexicographical Order)로 나열하라
-> 사전순으로 가장 빠른게 최대한 가장 앞에 오도록 만들되 순서를 바꿀수는 없고 중복은 제거해야 한다
-> 중복되는 것들중 가장 빠른 문자열을 만들 수 있는 것을 선택해야 한다

:param s: "cbacdcbc"
:return: "acdb"
'''

from collections import defaultdict

def solution(s):
    '''
    각 문자의 위치를 저장하고 정렬해서 가장 첫 문자를 기준으로 뒤에 높을지 앞에 높을지 결정한다
        -> 중복이 없는 값은 위치값을 기준으로 정한다

    정렬된 순서로 하니 leetcode가 ltcode로 나온다 letcod가 정답
    역정렬을해서 이전 값보다 앞으로 나오도록 정의해보자-> 실패
    '''
    overlap_del_dict = defaultdict(list)
    for idx, ch in enumerate(s):
        overlap_del_dict[ch].append(idx)

    overlap_del_arr = sorted(overlap_del_dict.items())

    # 사전순으로 가장 빠른 값을 기준으로 시작(제일 앞의 문자열은 중복이 있더라도 가장 앞의 값이 쓰인다)
    spot = overlap_del_arr[-1][1][0] # 2('a'의 인덱스)
    back = [(overlap_del_arr[-1][0], overlap_del_arr[-1][1][0])]
    front = []
    # prev_spot = 0

    print(overlap_del_arr)
    for ch, idx in overlap_del_arr[1:]: # 정렬된 순서
        back_num = False

        for i in idx:
            if spot < i:
                back_num = True
                back.append((ch, i))
                break

        if not back_num :
            front.append((ch, idx[-1]))

        # if back[-1][1] > prev_spot:
        #     back[-1][1] = idx[0]

    result = sorted(front+back, key=lambda x: x[1])
    print(result)

    return "".join([i for i, _ in result])


from collections import Counter

def answer_stack(s):
    counter, seen, stack = Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)

    return ''.join(stack)





print(answer_stack("leetcode"))