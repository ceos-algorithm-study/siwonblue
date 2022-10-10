# 럭키 스트레이트


data = list(map(int,list(input())))

def solve(data):
    middle = len(data)//2
    first = data[:middle]
    second = data[middle:]
    if sum(first) == sum(second):
        print('LUCKY')
    else:
        print('READY')
solve(data)