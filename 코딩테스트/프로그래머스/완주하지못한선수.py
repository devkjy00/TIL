# 총 참가자리스트와 완주자리스트를 비교 미완주자를 반환
# remove함수를 썻을 때 효율성 테스트를 통과하지 못했다
# 성능을 개선하기 위해 정렬하고 순차 비교를 했다

def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(0)
    for i, key in enumerate(participant):
        if key != completion[i]:
            return key