'''
class Time
    -> get_time() : 현재 시간 반환
    -> add_time() : 시간을 더한다
    -> check_time() : 시간을 검사한다, 늦지 않았으면 True


자 이렇게 되면 변경사항이 생기면 이 객체 안에서만 구현해주면 됩니다
'''


class Time:
  def __init__(self, hour, minute=0):
      self.hour = hour
      self.minute = minute

  def get_time(self):
      return f"{self.hour}시 {self.minute}분"

  def add_time(self, hour, minute=0):
      self.hour += hour
      self.minute += minute

      if minute >= 60:
          self.hour += 1
          self.minute -= 60

  def check_time(self, time_obj):
      if (time_obj.hour, time_obj.minute) <= (self.hour, self.minute):
          return True
      else:
          return False




class WiseMom:
    def __init__(self, time):
        self.time = Time(time)

    def commute(self, company):
        print("지금은", self.time.get_time(), "시 빨리 출근하자")
        print()
        company.check_commute_time(self.time)






class Uncle:
    def __init__(self, time):
        self.time = Time(time)

    def get_children_to_school(self, son):
        print("삼촌 : 지금은", self.time.get_time(), "시 이제 조카 깨우고 등원 시켜야겠다")
        print()
        self.time.add_time(son.never_listen())





class Son:
    def __init__(self):
        self.lazy_time = 1

    def never_listen(self):
        print("아들 : 가기싫어! 놀고싶어! 안해! 알고리ㅈ..아니 어린이집!@ 안해!! 싫어!!!")
        print(self.lazy_time, "시간동안 Son객체와 씨름하다가 겨우 등원 시켰다...")
        print()
        return self.lazy_time




class Company:
    def __init__(self, time):
        self.출근시간 = Time(time)

    def check_commute_time(self, time):
        print("----회사도착----")
        if self.출근시간.check_time(time):
            print("부장님 : 오 우리회사객체를 위해 준비된 객체로군요!!")
        else:
            raise Exception("부장님 : 아니 객체지향 세상에... 감히 누가 지각을 하였는가...")








와이스맘 = WiseMom(8)
백수삼촌 = Uncle(8)
말절대안듣는아들 = Son()
항해99 = Company(9)






백수삼촌.get_children_to_school(말절대안듣는아들)
와이스맘.commute(항해99)














'''

책임 분리를 잘 하는 팁...!!!
클래스를 정의할 때 변수가 아니라 메서드를 먼저 생각한다!!!
자동차 -> 바퀴, 창문 x
자동차 -> 시동켜기, 운전하기 o

-> 필요한 것만 가지게 되서 응집력을 높이고 책임을 생각하기 쉽다









제가 짠 코드는 정답이 아닙니다! 
다들 많은 코드를 접하시고 올바른 코드를 작성하시기를 바랍니다 !!!
'''