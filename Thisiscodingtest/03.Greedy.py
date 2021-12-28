# Chapter 03. 그리디



# 3-1 . 거스름돈 
n = 1260
count = 0 # 초기화

type = [500,100,50,10]

for coin in type:
    count += n//coin
    n %= coin



# 3-2 
n, m, k = map(int, input().split()) # n, m, k를 공백으로 구분하여 입력받기
data = list(map(int, input().split())) # n개의 수를 공백으로 구분하여 입력받기

data.sort()
first = data[n -1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

count = int(m/(k+1))* k # 가장 큰 수가 더해지는 횟수 계산
count += m %(k+1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second # 가장 작은 수 더하기

print(result)



# 3-3. minn() 함수를 이용하는 답안 예시
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) # 현재 줄에서 '가장 작은 수' 찾기
    result = max(result, min_value) # '가장 작은 수'들 중에서 가장 큰 수 찾기

print(result)



# 3-4. 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)



# 3-5
n, k = map(int, input().split())
result = 0

while n>= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n> 1:
    n -=1
    result += 1

print(result)



# 3-6
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n <k:
        break
    result +=1
    n //= k

result +=(n-1)
print(result)