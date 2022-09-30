# 문자열 압축

s = input()


# aabbccc => 2a2b3c

def solve(s):
    ans = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        test = s[0:step]
        cnt = 0
        for i in range(step, len(s), step):
            if test == s[i:i + step]:
                cnt += 1

            print('test', test)
            print('s[i:i+step]', s[i:i + step])


solve(s)