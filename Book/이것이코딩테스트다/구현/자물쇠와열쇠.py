# 격자 한칸의 크기가 1*1, N*N크기의 정사각 격자
# 열쇠는 M*M크기의 정사각형
# key 배열을 회전, 이동해서 lock배열의 0을 key의 1과 위치가 일치하도록
# key의 1의 위치가 lock의 1과 같은 위치가 되면 안됨


def rotate_a_matrix(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result

def check(new_lock):
    lock_length = len(new_lock)
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != i:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        key = rotate_a_matrix(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                
                if check(new_lock) == True:
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+i] -= key[i][j]
        
        return False
