
data = list(input())

def solve(data):
    num = 0
    str = []
    for i in range(len(data)):
        if ord(data[i]) < 58:
           num += int(data[i])
        else:
            str.append(data[i])
    str.sort()
    print(''.join(str), end='')
    print(num)
solve(data)


