def solution(num):
    answer = 0
    while num != 1 and answer < 500:
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        answer += 1
    return answer if num == 1 else -1


# 가독성을 위해서
# if answer >= 500: return -1 이 더 좋겠다

import unittest


class test_class(unittest.TestCase):
    def test_soultion(self):
        input = [6, 16, 626331]
        ouput = [8, 4, -1]
        for x, y in zip(input, ouput):
            self.assertEqual(solution(x), y)


test_class().test_soultion()
