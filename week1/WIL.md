# [이코테 Part3] 그리디 1번 : 모험가 길드

### ❓예제 입력

```python
# 예제 입력 1
5 
2 3 1 2 2 
# 예제 입력 2
6
2 3 1 2 2 3
# 예제 입력 3
11
1 1 2 2 2 3 3 3 3 4 6 
```

### 🔎 구현 코드

```python
n = int(input())
data = list(map(int, input().split()))
data.sort()
#print('data',data)

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
        if start+1 in temp:
            start +=1
            continue
        else:
            group.append(temp)
            cnt += 1
            data = data[start:]
    #print('group',group)
    #print('cnt',cnt)
solve(data)
```

### ‼️ 접근 방식

- 공포도가 큰 사람을 먼저?
    - 5, 1, 1, 1, 1 큰 사람부터 만들면 만들 수 있는 그룹의 최소값이 나옴
- 공포도가 작은 사람을 먼저
    - 만들 수 있는 그룹의 최대값은 여기서 나옴

### ✔️ 알고리즘

- 정렬
- 1의 개수 세서 카운트
- 1이 없는 리스트를 만들고 시작점 2부터 리스트를 2개씩 꺼냄
- 이때 해당 값보다 큰 값이 존재하면 start +=1 을 시키고 다시 반복
- 리스트의 최소값이 리스트의 길이보다 커질 때까지 계속 반복

### ☑︎ 회고
예외처리가 조금 힘들었다.

---

# [이코테 Part3] 그리디 2 : 곱하기 혹은 더하기

### ❓예제입력

### 🔎코드 구현

```python
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
```

### ‼️접근 방식

- 0이 있을 때 더해준다
- 1이 있을 때 더해준다

### ✔️알고리즘

- 처음 수에서 부터 그 다음 수를 더할지 곱할지만 판단해주면 됨

### ☑︎ 회고

> 문자열을 탐색할 때 반복문을 통해서 순서대로 가는 것을 잊지 말자!

---

# [이코테 Part3] 그리디 3 : 문자열 뒤집기

### ❓예제입력

### 🔎코드 구현

```python
data = input()

count0 = 0
count1 = 0

def solve(data):
    global count0, count1
    if data[0] == '0':
        count0 +=1 
    else:
        count1 +=1 
    for i in range(len(data)-1):
        if data[i] != data[i+1]:
            if data[i+1] == '1':
                count1 += 1 
            else:
                count0 += 1 
    print(count1, count0)

solve(data)
```

### ‼️접근 방식

- 0으로 모두 바뀌는 경우, 1로 모두 바뀌는 경우
- 둘 중에 적은 값이 답임
- 실제로 값을 바꿀 필요가 없고 카운트만 하면 되기때문에 복잡하게 생각하지 않아야 한다.


### ✔️알고리즘

- 처음 값을 저장
- 모든 값을 확인

### 시간분석

### 예외처리

### ☑︎ 회고

> 문자열 탐색은 반복문으로 하나씩 파악 \
BOJ 2138 ‘전구와 스위치’ 문제는 실제로 값을 바꿔줘야 하는 경우
>
---

# [이코테 Part3] 그리디 4 : 만들 수 없는 금액

### 🔎코드 구현

### ‼️접근 방식

- 1원부터 올라가면서 만들 수 있는지 파악?
    - 구현이 어려운데
- 최소값이 1보다 크다면 최소값 -1 이 답
- 모두 다 더한 값+1 보다 큰 값은 나올 수 없으니 그 값에서 시작해서 내려가면 되겠다.
    - 그걸 어떻게 구현해야할지 모르겠음
    - 합의 최대 값이 10억이 돼서 시간초과 받을 확률 높음

### ✔️알고리즘

- 알고리즘 자체를 이해 못 함

### 시간분석

### 예외처리

### ☑︎ 회고
아 이해를 못해서 그냥 넘어감

---

# [이코테 Part3] 그리디 5 : 볼링공 고르기

### ❓예제입력

### 🔎코드 구현

```python
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
```

### ‼️접근 방식

- 순서대로 뒤에 있는 것들을 판단하면 됨

### ✔️알고리즘

- 데이터 반복문 돌림
- 가장 앞의 값 추출과 그 뒤의 값으로 분리
- 뒤의 값 반복문 돌리면서 앞의 값과 일치하지 않을 때만 카운트

### 시간분석

### 예외처리

### ☑︎ 회고

> 이코테 문제는 답을 확인하기 어렵다. 실제 예외처리가 제대로 되었는지 확인할 길이 없어 아쉽다.

---

### ❓예제입력

### 🔎코드 구현

```python
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
```
# [이코테 Part3] 구현 7 : 럭키 스트레이트

### 🔎코드 구현

```python
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
```

### ‼️접근 방식

- 더하고 비교
- 문제가 쉬워서 시간 제한이 걸릴 것이라 판단하는데 답 제출이 없어서 확인을 못 하겠음

### ✔️알고리즘

- 짝수만 들어오니까 반 잘라서 다 더하면 됨

### 시간분석

- Slice, I[a:b], O(b-a) ⇒ N의 복잡도
- N의 범위는 1억, 파이썬 1초에 10억까지 커버가능하다고 하니 괜찮을 것 같음

### 예외처리

### ☑︎ 회고

> 시간 복잡도에 대한 계산이 두려웠다.

---

[이코테 Part3] 구현 8 : 문자열 재정렬

### 🔎코드 구현

```python
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
    print(''.join(str),end='')
    print(num)
solve(data)
```

### ‼️접근 방식

- ord() 를 이용해서 알파벳과 숫자를 구분
- 알파벳이면 리스트에 넣고 정렬
- 숫자면 다 더함
- 문자열로 합쳐서 출력

### ✔️알고리즘

### 시간분석

### 예외처리

### ☑︎ 회고

> 풀긴 했는데 맞게 푼지 모르겠다. 예외 처리가 확실하게 되었는지
>