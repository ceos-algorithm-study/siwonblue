# 곱하기 혹은 더하기

data = input()
result = int(data[0])

def solve(data):
    global result
    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or result <=1:
            result += num
        else:
            result *= num
    print(result)
solve(data)