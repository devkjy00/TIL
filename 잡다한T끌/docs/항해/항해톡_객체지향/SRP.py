'''
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
import Company, Son, SuperMom



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









# 잘 동작하고 있는 이 객체들의 협력에 요구사항변경이라는 큰 재앙이 들이 닥칩니다






















'''
한 가지 책임만 가지는 WiseMom 객체

class WiseMom
    -> commute() : 직장으로 출근한다

# 노는 동생한테 용돈 주고 아들의 등원을 맡긴다
class Uncle
    -> get_children_to_school() : 자녀들을 어린이집에 등원시킨다
'''