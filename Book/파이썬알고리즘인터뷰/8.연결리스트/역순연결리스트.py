'''
https://leetcode.com/problems/reverse-linked-list/

연결 리스트를 뒤집어라

:param head: 1->2->3->4->5->None
:return: 5->4->3->2->1->None
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

result = []

def solution(head):
    '''
    역순서로 다시 연결하는 것은 성공했지만 반환값의 위치가 마지막이 되어서 값을 확인 할 수 없었다
        -> 전역 값을 만들어서 역순서의 첫번째 값의 위치를 대입했다

    재귀함수가 완성된 값을 반환하도록 만들 수 있는지 고려할 필요
    '''
    if not head:
        return
    if not head.next:
        value = ListNode(head.val)
        result.append(value)
        return value

    reversed_head = solution(head.next)
    reversed_head.next = head
    head.next = None

    return head




def answer_recursive(head):
    '''
    디폴트 값을 이용해서 재귀함수의 인자값을 유연하게 만들었다
    이전 노드를 다음 호출로 넘겨서 다음 노드의 next에 대입해줬다
    '''
    def reverse(node, prev=None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

def answer_for(head):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

solution(ListNode(1, ListNode(2, ListNode(3, ListNode(4, (ListNode(5)))))))
result = result[0] if result else None

while result:
    print(result.val)
    result = result.next

