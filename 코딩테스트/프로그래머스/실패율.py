N = 10
stages = [1, 2, 3, 4, 4, 4, 5, 6, 2, 6, 3, 4]


def fail_pct(x):
    fail = stages.count(x)
    clear = [i for i in stages if i > x]
    if fail == 0:
        print(x, 0)
        return 0
    elif (clear_num := len(clear) + fail) != 0:
        print(x, "실패율", fail, "/", clear_num, fail / clear_num)
        return fail / clear_num
    else:
        print(x, 1)
        return 1


answer = sorted(list(range(1, N + 1)), reverse=True, key=fail_pct)

print(answer)

# 연산을 다르게 하는 방법: 실패한스테이지길이/전체스테이지길이 -> 전체스테이지길이 - 실패스테이지길이
