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
