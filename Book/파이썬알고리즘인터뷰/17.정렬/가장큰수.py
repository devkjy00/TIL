'''
https://leetcode.com/problems/largest-number/

항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라


:param nums: [10, 2]
:return: "210"
'''


def solution(nums):
    nums_str = []
    for num in nums:
        # if num > 9:
        #     nums_str.append(tuple([i for i in str(num)]))
        #     continue
        # else:
        nums_str.append(str(num))

    nums_str.sort(reverse=True)

    print(nums_str)







solution([3, 30, 34, 5, 9])