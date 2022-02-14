# 학생 N명, 
# 국, 영, 수 점수
# 국어 점수가 내림차순
# 국어가 같으면 영어 올림차순
# 둘다 같으면 수학 내림차순
# 모든 점수가 같으면 이름순서 오름차순

# 정렬후 학생 이름 출력

n = 12
student_score = [["Junkyu", 50, 60, 100],
                ["Sangkeun", 80, 60, 50],
                ["Sunyoung", 80, 70, 100],
                ["Soong", 50, 60, 90],
                ["Haebin", 50, 60, 100],
                ["Kangsoo", 60, 80, 100],
                ["Donghyuk", 80, 60, 100],
                ["Sei", 70, 70, 70],
                ["Wonseob", 70, 70, 90],
                ["Sanghyun", 70, 70, 80],
                ["nsj", 80, 80, 80],
                ["Taewhan", 50, 60, 90]]

student_score.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
[print(i[0]) for i in student_score]
