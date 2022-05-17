'''
https://leetcode.com/problems/implement-queue-using-stacks/

스택을 이용해 push, pop, peek, empty을 지원하는 큐를 구현하라

'''

class MyQueue:
    def __init__(self):
        self.stack = []
        self.stack_received = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.stack_received.append(self.stack.pop())

        que_pop = self.stack_received.pop()

        while self.stack_received:
            self.stack.append(self.stack_received.pop())

        return que_pop


    def peek(self) -> int:
        while self.stack:
            self.stack_received.append(self.stack.pop())

        que_peek = self.stack_received[-1]

        while self.stack_received:
            self.stack.append(self.stack_received.pop())

        return que_peek

    def empty(self) -> bool:
        return False if self.stack else True



que = MyQueue()
que.push(3)
que.push(2)
print(que.empty())
print(que.pop())
print(que.peek())
print(que.pop())
print(que.empty())
