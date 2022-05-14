'''
https://leetcode.com/problems/palindrome-linked-list/

연결 리스트가 팰린드롬 구조인지 판별하라

:param head: [1, 2, 2, 1]
:return: true
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_arr(head: ListNode):
    arr = []
    while True:
        arr.append(head.val)
        if head.next:
            head = head.next
        else:
            break

    return arr

def solution(head: ListNode):
    arr = get_arr(head)
    return True if arr == arr[::-1] else False



