'''
https://leetcode.com/problems/group-anagrams/

에너그램이란 문자를 재배열해서 다른 뜻을 가진 단어로 바꾸는 것이다

:param strs: ["eat","tea","tan","ate","nat","bat"]
:return : [["bat"],["nat","tan"],["ate","eat","tea"]]

-> 정렬된 문자를 키값으로 사용해서 값을 추가, 추가구현 없이 그룹화를 했다
'''
from collections import defaultdict

def solution(strs: list[str]) -> list[list[str]]:
    sorted_str = defaultdict(list)
    for str in strs:
        sorted_str["".join(sorted(str))].append(str)

    # return [var for var in sorted_str.values()]
    return list(sorted_str.values())

print(solution(["eat","tea","tan","ate","nat","bat"]))