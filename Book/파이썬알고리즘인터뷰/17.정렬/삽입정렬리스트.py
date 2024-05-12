'''
https://leetcode.com/problems/insertion-sort-list/

연결리스트를 삽입정렬로 정렬하라

:param head = [4, 2, 1, 3]
:return: [1, 2, 3, 4]
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def solution(head):
    '''
    포인터가 앞으로 갔다가 뒤로 갔다가 하면서 순서대로 self.next값을 바꾼다
    '''
    while head:

        head = head.next















solution(ListNode(4, ListNode(2, ListNode(1, ListNode(3)))))




