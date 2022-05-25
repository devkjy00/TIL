'''




개발자의 세상 만만치 않습니다.... 부트캠프를 떠나 야생의 개발세상에 들어가면 별의 별일을 다 겪는다고 합니다....(윤교님 왈)












자 한번 짜놓은 코드가 영원할 까요..??  아니져...
세상은 변하고 사람들의 요구사항도 변하고 기술도 변합니다..
만약 아무런 계획없이 구현만 되는 코드를 짠다면 그 코드는 시한폭탄과 마찬가지입니다..















제 경험을 이야기 하자면
코딩에 재미 들려서 밤을 새워 첫 토이프로젝트를 완성시켰을 때가 기억이 납니다
얼마 후 좋은 아이디어가 떠올라서 변경을 하려고 다시 코드를 열었을 때 깨달았습니다
이 코드는 가망이 없다는 것을..... 이미 이 코드는 강을 건너 버렸다는 것을.....

이런 코드를 '스파게티 코드'라고 합니다.. 한입 먹으려고 뜨면 엉켜있는 모든 면이 같이 올라오죠... 우욱 그때가 생각나...;;;














그래서 많고 많은 지식중 객체지향의 한가지 원칙을 설명하겠습니다
* 단일 책임 원칙(Single Responsiblity Principle)*
    - 클래스든 메서드든 한가지의 책임만 가져야한다는 원칙
    - 여러 책임을 가진 객체의 경우 하나의 책임에 대한 변경은 다른 책임의 수정을 발생시킵니다
    - 그래서 책임은 곧 변경 사유가 됩니다


이게 무슨 말일 까요...? 코드로 확인해 보죠

















**** 이해를 위해 반 억지로 짜 봤습니다.. ****

여기는 객체지향의 세상....
2가지 책임을 가진 SuperMon 객체

class SuperMom
    -> commute() : 직장으로 출근한다
    -> get_children_to_school() : 자녀들을 어린이집에 등원시킨다

class Company
    -> check_commute_time() : 직원의 출근 시간을 체크

class Son
    -> never_listen(): 엄마말 안듣기 시전, 시간을 지체시킨다
'''






class SuperMom:
    def __init__(self):
        self.time = 8

    def commute(self, company):
        company.check_commute_time(self.time)

    def get_children_to_school(self, son):
        self.time += son.never_listen()





class Company:
    def __init__(self, time):
        self.commute_time = time

    def check_commute_time(self, time):
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
        return self.lazy_time

















# 출근시간을 매개변수로 회사객체를 생성
네이버 = Company(9)


# 2가지일을 하는 수퍼맘 객체를 생성
수퍼맘 = SuperMom()


# 말 안듣는 아들 객체를 생성
말안듣는아들 = Son()





# 아들을 등원 시킨다
수퍼맘.get_children_to_school(말안듣는아들)



# 회사에 출근한다
수퍼맘.commute(네이버)












# 잘 동작하는 것 처럼 보이는 이 객체들의 협력에 요구사항변경이라는 큰 재앙이 들이 닥칩니다
# 말 안듣는 아들은 이제부터는 더 때를 써서 2시간동안 시간을 지체시키기로 합니다





















'''
한 가지 책임만 가지는 WiseMom 객체

class WiseMom
    -> commute() : 직장으로 출근한다

# 노는 동생한테 용돈 주고 아들의 등원을 맡긴다
class Uncle
    -> get_children_to_school() : 자녀들을 어린이집에 등원시킨다
'''


class WiseMom:
    def __init__(self):
        self.time = 8

    def commute(self, company):
        company.check_commute_time(self.time)





class Uncle:
    def __init__(self):
        self.time = 8

    def get_children_to_school(self, son):
        self.time += son.never_listen()








# 객체 생성
와이스맘 = WiseMom()
백수삼촌 = Uncle()
말절대안듣는아들 = Son()
카카오 = Company(9)






백수삼촌.get_children_to_school(말절대안듣는아들)

와이스맘.commute(카카오)

# 책임을 분리해서 Son객체가 아무리 말썽을 부려도 WiseMom객체의 출근에는 문제가 없죠












'''
자 이해가 됬을까요????


그런데 자세히 보니 분리하면 좋을 책임이 하나더 있는 거 같습니다!!


객체들을 살펴보니 time변수를 서로 두루뭉술하게 사용하고 있습니다!! 
만약 time을 9가 아니라 9시 30분으로 표현하려면 어떻게 하죠???
모든 객체를 변경해야하는 대 참사가 벌어집니다...


자 그러면 시간을 책임지는 객체를 만들어 줍시다!
'''

