'''
https://leetcode.com/problems/implement-stack-using-queues/

큐를 이용해 push, pop, top, empty를 지원하는 스택을 구현하라
'''
import collections

class MyStack:
    def __init__(self):
        self._q = collections.deque()

    def push(self, x: int) -> None:
        self._q.append(x)

    def pop(self) -> int:
        return self._q.pop()

    def top(self) -> int:
        return self._q[-1]

    def empty(self) -> bool:
        return False if self._q else True

stack = MyStack()
stack.push(2)
print(stack.empty())
print(stack.top())
print(stack.pop())
print(stack.empty())
