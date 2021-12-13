def solution(n, m):
    answer = []
    for i in range(n,0,-1):
        if n%i or m%i:
            continue
        else: 
            answer.append(i)
            break
    for i in range(m,m*100,+m):
        if i%n or i%m:
            continue
        else:
            answer.append(i)
            break
    return answer


import unittest


class test_class(unittest.TestCase):
    def test_soultion(self):
        self.assertEqual(
            solution(2,5),[1,10]
        )


test_class().test_soultion()
