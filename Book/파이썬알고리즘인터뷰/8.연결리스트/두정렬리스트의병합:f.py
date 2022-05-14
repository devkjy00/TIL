'''
https://leetcode.com/problems/merge-two-sorted-lists/

정렬되어 있는 두연결 리스트를 합쳐라

:param list1: [1, 2, 4]
:param list2: [2, 3, 4]
:return: [1, 1, 2, 3, 4, 4]
'''
# 정의된 클래스를 인풋값으로 받는다
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(li_1, li_2):
    '''
    하나씩 꺼내서 val을 비교하고 순서대로 next에 대입
    - li_1.val , li_2.val 를 비교
    - 더 작은 값을 merged에 대입
    - li_1.next.val, li_2.val 를 비교
    - 더 작은 값을 merged.next에 대입 (merged= merged.next)

    -> None 일때 처리를 못했다
    '''
    merged_list = ListNode(-1)

    while li_1:
        if li_1.val < li_2.val:
            merged_list = li_1
            li_1 = li_1.next
        else:
            merged_list = li_2
            li_2 = li_2.next

        print(merged_list.val)
        merged_list = merged_list.next


# solution(ListNode(1, ListNode(3)), ListNode(2, ListNode(4)))

def answer(l1, l2):
    '''
    더 작은 값이나 None이 아닌 값을 l1으로 만들어 주고
    한번 더 l1이 None이 아니면 l1을 반환, l1.next에 대입
    '''

    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1

    if l1:
        l1.next = answer(l1.next, l2)
        print(l1.val)

    return l1

answer(ListNode(1, ListNode(3)), ListNode(2, ListNode(4)))
