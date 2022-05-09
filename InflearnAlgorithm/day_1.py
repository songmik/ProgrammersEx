# 파이썬 기초 문법

# 1. 변수와 출력함수
'''
 1). 변수명 정하기
    - 영문과 숫자, _로 이루어진다.
    - 대소문자를 구분한다.
    - 문자나, _로 시작한다.
    - 특수문자를 사용하면 안된다. (&, % 등)
    - 키워드를 사용하면 안된다. (it, for 등)
'''
# 2. 변수 입력과 연산자

# 3. 조건문(if분기문, 다중if문)

# 4. 반복문(for, while, break, continue)


'''
반복문을 이용한 문제풀이
1. 1부터 N까지 홀수출력하기
n = int(input())
for i in range(1, n+1): 
    if i%2==1:
        print(i) 

2. 1부터 N까지의 합 구하기
n = int(input())
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)

3. N의 약수 출력하기
n = int(input())
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=' ') // 줄 바꾸지 않고 옆으로 출력된다.
        




'''
# 5. 반복문을 이용한 문제 풀이
# 6. 중첩반목문(2중 for문)

'''

for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()


** 별찍기
for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()


** 거꾸로 별찍기
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()

'''
# 7. 문자열과 내장함수

'''
함수.upper() -> 글자를 다 대문자로 
함수.lower() -> 글자를 다 소문자로
함수.find('') -> ''안에 찾고 싶은 변수를 적으면 인덱스 번호를 출력함(제일 앞에 있는 인덱스 번호가 선택)
함수.count('') -> ''안에 있는 것이 몇 개나 있는지 출력
함수[:2] -> 범위를 입력 0~1번까지 출력하는 것 
len(함수) : 길이를 구해서 출력
함수.isupper() : 대문자이면 true   
함수.islower() : 소문자이면 true 
함수.isalpha() : 알파벳만 출력 
ord(함수) : 함수의 아스키 넘버를 출력
chr(함수) : 숫자에 대응하는 아스키 문자를 출력



'''
# 8. 리스트와 내장함수_1
'''

1. 빈 리스트 만들기
 1). a = []
 2). a = list() -> list(range(1,11)) 이라고 하면, 1~10까지의 숫자가 담긴 배열이 만들어짐
2. a.append() : a 배열에 () 안에 있는 것을 더한다
3. a.insert(x,y) : x번 인덱스 지점에 y를 삽입한다.
4. a.pop() : a 배열에서 ()안에 있는 것을 없앰(꺼냄)
5. a.remove() : a 배열에서 ()안에 있는 값을 지움
6. print(a.index()) : 괄호안에 있는 값의 인덱스 위치를 알고싶을 때
7. sum : 배열 안에 값을 다 더해줌, max : 배열 중에서 가장 큰 수, min
8. r.shuffle(a) : import random as r 을 사용하여 a 배열 안에 있는 값을 섞어준다.



'''
# 9. 리스트와 내장함수_2
# 10. 2차원 리스트 생성과 접근
# 11. 함수만들기
# 12. 람다함수



# 코드 구현력 기르기

# 1. 환경설정 및 K번째 약수 풀이
'''
n, k = map(int, input().split())  // input()으로 받은 숫자들이 띄어쓰기가 되어 있으니까 split으로 빈칸을 잘라주고, 앞에 있는 int로 바꿔준다는 의미
cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt+=1
    if cnt == k:
        print(i)
        break
else:
    print(-1)



'''
