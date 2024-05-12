'''
https://leetcode.com/problems/odd-even-linked-list/

연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라, 공간 복잡도 O(1), 시간 복잡도 O(n)

:param head: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
:return: 1 -> 3 -> 5 -> 2 -> 4 -> NULL
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(head):
    '''
    for문으로 인덱스를 2 씩 올려서 한번에 홀수 짝수번을 처리하자 -> 마지막 인덱스가 홀수인지 짝수인지 알수 없어서 오류예상
    while문으로 짝수 홀수를 구분해서 각 각의 연결리스트에 연결하자
    짝수일 떄는 홀수의 next, 홀수 일때는 짝수의 next를 None으로 할당 -> 해당 시점의 head.next 값을 변경시키지 않는 방법
    '''

    odd_time = False
    odd, even = first_node, second_node = ListNode(), ListNode()


    while head:
        if odd_time := not odd_time:
            odd.next = head
            odd, even.next = odd.next, None
        else:
            even.next = head
            even, odd.next = even.next, None

        head = head.next

    odd.next = second_node.next

    return first_node.next

result = solution(ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7))))))))

while result:
    print(result.val)
    result = result.next


def answer(head):
    '''
    짝수, 홀수 번째를 연결하는 규칙을 이용해서 head.next = head.next.next로 한 칸을 건너뛰어서 바로 연결했다
        -> 자연스럽게 마지막에 None이 대입된다
    '''
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head