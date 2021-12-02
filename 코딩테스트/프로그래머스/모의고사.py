# 정답을 전부 찍었을 때 가장 많이 맞춘 사람 찾기

answers = [1, 2, 3, 4, 5]
people = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
answer = {1: 0, 2: 0, 3: 0}
for i, key in enumerate(answers):
    for j, d in zip([0, 1, 2], [5, 8, 10]):
        if key == people[j][i % d]:
            answer[j + 1] += 1
answer = sorted(answer.items(), reverse=True, key=lambda x: x[1])

answer = [answer[i][0] for i in [0, 1, 2] if answer[0][1] == answer[i][1]]
print(answer)
