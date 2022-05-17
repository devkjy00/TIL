'''
https://leetcode.com/problems/design-circular-queue/

원형 큐를 디자인하라
'''


class MyCircularQueue:
    def __init__(self, k: int):
        self.length = k
        self.queue = []

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.length:
            self.queue.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.queue:
            del self.queue[0]
            return True
        else:
            return False

    def Front(self) -> int:
        return self.queue[0] if self.queue else -1

    def Rear(self) -> int:
        return self.queue[-1] if self.queue else -1

    def isEmpty(self) -> bool:
        return False if self.queue else True

    def isFull(self) -> bool:
        return True if len(self.queue) == self.length else False


circle_que = MyCircularQueue(5)
print(circle_que.enQueue(10))
print(circle_que.enQueue(20))
print(circle_que.enQueue(30))
print(circle_que.enQueue(40))
print(circle_que.Rear())
print(circle_que.isFull())
print(circle_que.deQueue())
print(circle_que.deQueue())
print(circle_que.enQueue(50))
print(circle_que.enQueue(60))
print(circle_que.Rear())
print(circle_que.Front())
