# 모험가 길드

n = int(input())
data = list(map(int, input().split()))
data.sort()

def check(start,temp):
    for v in temp:
        if start < v:
            return True
    return False

def solve(data):
    cnt = 0
    group = []
    cnt += data.count(1)
    data = data[cnt:]
    # print(cnt)
    # print(data)
    start = 2
    while len(data) !=0 and min(data) < len(data):
        temp = data[0:start]
        if len(temp) < start:
            break
        if check(start,temp):
            start +=1
            continue
        else:
            # group.append(temp)
            cnt += 1
            data = data[start:]
    # print(group)
    print(cnt)
solve(data)







