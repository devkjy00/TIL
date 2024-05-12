'''
https://leetcode.com/problems/3sum/

배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라

:param nums: [-1, 0, 1, 2, -1, -4]
:return: [[-1, 0, 1], [-1, -1, 2]]
'''

def answer(nums):
    '''
    투 포인터를 이용해서 시간복잡도를 줄인 풀이이다
    1. 3개의 포인터가 필요한 상황
    2. 첫번째는 하나의 for문으로 만들고 그 다음 2개의 포인터는 내부의 하나의 while문으로 만들었다
    3. 정렬을 해서 값이 클 때와 작을 때에 포인터를 옮겨 줬다
    '''
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return result


print(answer([-1, 0, 1, 2, -1, -4]))

