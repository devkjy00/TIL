# 격자 한칸의 크기가 1*1, N*N크기의 정사각 격자
# 열쇠는 M*M크기의 정사각형
# key 배열을 회전, 이동해서 lock배열의 0을 key의 1과 위치가 일치하도록
# key의 1의 위치가 lock의 1과 같은 위치가 되면 안됨




def solution(key, lock):
    key_count = count_vector(key, 1)
    lock_count = count_vector(lock, 0)
    if key_count < lock_count: 
        return False
    
    while True:
        if match_key_lock(key, lock):
            return True
        



def count_vector(source: list, finding: int):
    return sum([i.count(finding) for i in source])

def match_key_lock(key: list, lock: list):
    for i in range(lock):
        for j in range(lock[0]):
            lock[i][j] += key[i][j]
    
    if not lock.count(0) and not lock.count(2):
        return True
    else: return False

def move_key(key, way):

def rotate_key(key: list) -> list:
    temp_key = [[] for _ in range(len(key))]
    for i in key[::-1]:
        idx = 0
        for j in i:
            temp_key[idx].append(j)
            idx += 1
    return temp_key

key = [[0, 0, 0],
        [1, 0, 0],
        [0, 1, 1]]
    
lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

print(solution(key, lock))