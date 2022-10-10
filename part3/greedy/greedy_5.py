# 볼링공 고르기

n, m = map(int, input().split())
data = list(map(int, input().split()))

def solve(data):
    ans = 0
    for i in range(len(data)-1):
        temp = data[i+1:]
        cnt = 0
        for v in temp:
            if data[i] != v:
                cnt +=1
            else:
                continue
        ans += cnt
    print(ans)
solve(data)
