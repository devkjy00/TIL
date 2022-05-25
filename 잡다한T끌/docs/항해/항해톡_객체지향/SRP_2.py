'''

한 가지 책임만 가지는 WiseMom 객체

class WiseMom
    -> commute() : 직장으로 출근한다

노는 동생한테 용돈 주고 아들의 등원을 맡긴다
class Uncle
    -> get_children_to_school() : 자녀들을 어린이집에 등원시킨다
'''





# class SuperMom:
#     def __init__(self):
#         self.time = 8
#
#     def commute(self, company):
#         company.check_commute_time(self.time)
#
#     def get_children_to_school(self, son):
#         self.time += son.never_listen()



















class Son:
    def __init__(self):
        self.lazy_time = 4

    def never_listen(self):
        print("아들 : 가기싫어! 놀고싶어! 안해! 알고리ㅈ..아니 어린이집!@ 안해!! 싫어!!!")
        print(self.lazy_time, "시간동안 Son객체와 씨름하다가 겨우 등원 시켰다...")
        print()
        return self.lazy_time





class Company:
    def __init__(self, time):
        self.commute_time = time

    def check_commute_time(self, time):
        if time == self.commute_time:
            print("부장님 : 자 WiseMom 객체님, 하루 일과를 시작하세요")
        elif time <= self.commute_time:
            print("부장님 : 오 우리회사객체를 위해 준비된 객체로군요!!")
        else:
            raise Exception("부장님 : 아니 객체지향 세상에... 감히 누가 지각을 하였는가...")











# 객체 생성


















# 책임을 분리해서 Son객체가 아무리 말썽을 부려도 WiseMom객체의 출근에는 문제가 없죠









'''
자 이해가 됬을까요????


그런데 자세히 보니 분리하면 좋을 책임이 하나더 있는 거 같습니다!!


객체들을 살펴보니 time변수를 서로 두루뭉하게 사용하고 있습니다!! 
만약 time을 9가 아니라 9시 30분으로 표현하려면 어떻게 하죠???
time을 사용하는 모든 객체를 변경해야하는 대 참사가 벌어집니다...


자 그러면 시간을 책임지는 객체를 만들어 줍시다!
'''

