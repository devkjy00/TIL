log_list = list(map(int,input()[:]))
if len(log_list) < 2:
    log_list.append(0)
count = 0
while True:
    log_list.append(int(str(sum(log_list[-2:]))[-1]))
    count += 1
    if log_list[-2:] == log_list[:2]:
        print(count)
        break

