import functools


def solution(x):
    x_list = map(int, list(str(x)))
    added_num = functools.reduce(lambda x, y: x + y, x_list)
    return x % added_num == 0


# sum()의 기능을 착각. 리스트가 아닌 리터럴값 반환
# added_num = sum(x_list) 로 간단하게 할 수 있다

import unittest


class test_class(unittest.TestCase):
    def test_soultion(self):
        self.assertEqual(solution(10), True)
        self.assertEqual(solution(11), False)


test_class().test_soultion()
