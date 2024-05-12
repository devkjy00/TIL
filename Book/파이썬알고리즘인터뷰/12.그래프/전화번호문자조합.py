'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

:param digits: "23"
:return: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''
import itertools

def solution(digits):
    if not digits:
        return

    num_to_ch = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }
    result = itertools.product(*[num_to_ch[int(i)]
                                for i in digits])
    return ["".join(i) for i in result]


def answer(digits):
    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)


print(solution("234"))