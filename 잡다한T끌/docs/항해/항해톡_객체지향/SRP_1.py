'''




개발자의 세상 만만치 않습니다.... 부트캠프를 떠나 야생의 개발세상에 들어가면 별의 별일을 다 겪는다고 합니다....(윤교님 왈)












한번 짜놓은 코드가 영원할 까요..??  아니져...
세상은 변하고 사람들의 요구사항도 변하고 기술도 변합니다..
만약 아무런 계획없이 구현만 되는 코드를 짠다면 그 코드는 시한폭탄과 마찬가지입니다..















제 경험을 이야기 하자면
코딩에 재미 들려서 밤을 새워 첫 토이프로젝트를 완성시켰을 때가 기억이 납니다
얼마 후 좋은 아이디어가 떠올라서 변경을 하려고 다시 코드를 열었을 때 깨달았습니다
이 코드는 가망이 없다는 것을..... 이미 이 코드는 강을 건너 버렸다는 것을.....

이런 코드를 '스파게티 코드'라고 합니다.. 작은변경을 하려고 하면 엉켜있는 모든 코드가 같이 올라오죠... 우욱 그때가 생각나...;;;














그래서 많고 많은 지식중 객체지향의 한가지 원칙을 설명하겠습니다
* 단일 책임 원칙(Single Responsiblity Principle)*
    - 객체는 한가지의 책임만 가져야한다는 원칙
    - 여러 책임을 가진 객체의 경우 하나의 책임에 대한 변경은 다른 책임의 수정을 발생시킵니다
    - 책임은 곧 변경 사유 입니다


이게 무슨 말일 까요...? 코드로 확인해 보죠

















**** 이해를 위해 반 억지로 짜 봤습니다.. ****

여기는 객체지향의 세상....
2가지 책임을 가진 SuperMom 객체

class SuperMom
    -> commute() : 직장으로 출근한다
    -> get_children_to_school() : 자녀들을 어린이집에 등원시킨다

class Company
    -> check_commute_time() : 직원의 출근 시간을 체크

class Son
    -> never_listen(): 엄마말 안듣기 시전, 시간을 지체시킨다
'''










class SuperMom:
    def __init__(self, time):
        self.time = time

    def commute(self, company):
        print("지금은", self.time, "시 빨리 출근하자")
        print()
        company.check_commute_time(self.time)

    def get_children_to_school(self, son):
        print("지금은", self.time, "시 이제 아들 깨우고 등원 시켜야겠다")
        print()
        self.time += son.never_listen()




class Company:
    def __init__(self, time):
        self.commute_time = time

    def check_commute_time(self, time):
        print("----회사도착----")
        if time == self.commute_time:
            print("부장님 : 자 SuperMom 객체님, 하루 일과를 시작하세요")
        elif time <= self.commute_time:
            print("부장님 : 오 우리회사객체를 위해 준비된 객체로군요!!")
        else:
            raise Exception("부장님 : 아니 객체지향 세상에... 감히 누가 지각을 하였는가...")




class Son:
    def __init__(self):
        self.lazy_time = 1

    def never_listen(self):
        print("아들 : 가기싫어! 놀고싶어! 안해! 알고리ㅈ..아니 어린이집!@ 안해!! 싫어!!!")
        print(self.lazy_time, "시간동안 Son객체와 씨름하다가 겨우 등원 시켰다...")
        print()
        return self.lazy_time














# 2가지일을 하는 수퍼맘 객체를 생성


# 말 안듣는 아들 객체를 생성


# 출근시간을 매개변수로 회사객체를 생성

















# 아들을 등원 시킨다



# 회사에 출근한다













# 잘 동작하는 것 처럼 보이는 이 객체들의 협력에 요구사항변경이라는 큰 재앙이 들이 닥칩니다
# 말 안듣는 아들은 이제부터는 더 때를 써서 2시간동안 시간을 지체시키기로 합니다





















