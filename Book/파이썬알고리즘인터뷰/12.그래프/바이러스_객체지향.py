'''
절차지향적으로 풀었던 바이러스문제를 객체지향적으로 풀어보았다
    -> 데이터와 함수를 하나로 묶는다


class VirusComputer
    - infect : 컴퓨터를 상태를 변경시켜서 감염시킨다

class Computer
    - communicate : 연결된 Computer 객체들에게 자신의 상태를 적용시킨다
    - link : Computer 객체 연결 정보를 저장

class Admin
    - set_computers : Computer 객체를 생성한다
    - connect : 입력받은 연결 정보로 Computer 객체를 연결한다
    - infection_check : 감염된 Computer 객체를 센다

33980kb, 76ms
'''
from pprint import pprint











class VirusComputer:
    @staticmethod
    def infect(computer):               # 감염시킬 Computer 객체를 매개변수로 받는다
        computer.status = "infected"    # Computer 객체의 상태값을 바꿔서 감염여부를 정한다
        computer.communicate()          # 연결된 모든 객체가 감염되도록 한다

















class Computer:
    def __init__(self, name):
        self.name = name
        self.status = "working"     # infection_table 역할을 하는 값
        self.linked_computers = []  # pc_link_table 역할을 하는 값

    def communicate(self):          # 재귀함수 역할, 연결된 객체의 메서드를 호출
        for com in self.linked_computers:
            if com.status != self.status:
                com.status = self.status
                com.communicate()

    def link(self, computer):       # 연결할 Computer 객체를 받아서 저장한다
        self.linked_computers.append(computer)

    def __str__(self):
        return self.name








class Admin:
    def __init__(self):
        self.computers = None

    def set_computer(self, computer_qty):
        self.computers = [Computer("{0}번 PC".format(i)) for i in range(computer_qty)]

    def connect(self, *link): # 컴퓨터 연결 구조를 2차원 리스트로 나타낸 것과 같은 역할
        for i, j in link:
            i -= 1
            j -= 1
            self.computers[i].link(self.computers[j])
            self.computers[j].link(self.computers[i])

    def infection_check(self):
        count = 0
        for com in self.computers:
            if com.status == "infected":
                count += 1

        return count







# 관리자가 초기 셋업을 해준다 (컴퓨터 객체 생성, 연결)
관리자_A = Admin()
관리자_A.set_computer(7)
관리자_A.connect([1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7])



# print("컴퓨터의 상태")
# [print(com,":", com.status) for com in 관리자_A.computers]


# print("컴퓨터의 연결상태")
# for com in 관리자_A.computers:
#     print(com, "와 연결된:", end=" ")
#     for linked in com.linked_computers:
#         print(linked, end=", ")
#     print()











# 바이러스 컴퓨터가 관리자_A의 컴퓨터를 감염시킨다
VirusComputer.infect(관리자_A.computers[0])
# print("컴퓨터의 상태")
# [print(com,":", com.status) for com in 관리자_A.computers]














# 관리자가 감염된 컴퓨터의 개수를 세어서 반환한다, 첫번째 컴퓨터 포함
# print(관리자_A.infection_check())







# 결론: 객체지향적으로 푸니까 더 재밌네요.. 하하 시간가는 줄 모르고...

