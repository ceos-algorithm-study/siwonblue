# 문자열 뒤집기

data = input()

count0 = 0
count1 = 0

def solve(data):
    global count0, count1
    if data[0] == '0':
        count0 +=1 # 0을 1로 바꾸는 것
    else:
        count1 +=1 # 1을 0로 바꾸는 것
    for i in range(len(data)-1):
        if data[i] != data[i+1]:
            if data[i+1] == '1':
                count1 += 1 # 1을 0로 바꾸는 것
            else:
                count0 += 1 # 0을 1로 바꾸는 것
    print(count1, count0)

solve(data)
