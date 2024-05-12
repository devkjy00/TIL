'''
https://programmers.co.kr/learn/courses/30/lessons/43165

:param dirs: "ULURRDLLU"
:return: 7


그래프 문제에서는 항상 방향성을 고려하자
'''


def solution(dirs):
    move = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}

    visited = set()
    coordinate = [0, 0]
    for dir in dirs:
        x, y = move[dir]
        if -5 <= coordinate[0]+x <= 5 and -5 <= coordinate[1]+y <= 5:
            visited.add((coordinate[0], coordinate[1], coordinate[0] + x, coordinate[1] + y))
            visited.add((coordinate[0]+x, coordinate[1]+y, coordinate[0], coordinate[1]))
            coordinate[0] += x
            coordinate[1] += y
            print(coordinate)
    print(visited)
    return len(visited)//2


assert solution("ULURRDLLU") == 7
assert solution("LULLLLLU") == 7