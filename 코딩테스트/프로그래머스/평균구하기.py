def solution(arr):
    return sum(arr) / len(arr)


import unittest


class test_class(unittest.TestCase):
    def test_soultion(self):
        self.assertEqual(solution([1, 2, 3, 4]), 2.5)
        self.assertEqual(solution([5, 5]), 5)


test_class().test_soultion()
