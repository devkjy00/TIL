import unittest


def solution(phone_number):
    answer = "*" * (len(phone_number) - 4) + phone_number[-4:]
    return answer


class test_class(unittest.TestCase):
    def test_soultion(self):
        self.assertEqual(solution("01033334444"), "*******4444")


test_class().test_soultion()
