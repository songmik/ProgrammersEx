# 계산 문제를 맞히는 게임
import random

def make_question():
    a = random.randint(1,40)
    b = random.randint(1,20)
    op = random.randint(1,3)

    q = str(a)

    if op == 1:
        q = q + '+'
    if op == 2:
        q = q + '-'
    if op == 3:
        q = q + '*'

    q = q + str(b)
    return q

sc1 = 0 # 정답과 오답 횟수를 저장할 변수를 0으로 초기화함
sc2 = 0

for x in range(5):
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans) # 입력받은 정답을 정수로 바꿈

    if eval(q) == r: # 컴퓨터가 계산한 값과 나의 입력값을 비교
        print("정답1")
        sc1 = sc1 + 1 # 정답일수록 정답 갯수가 +1 됨
    else:
        print("오답")
        sc2 = sc2 + 1

print("정답: ", sc1, "오답 : ", sc2)
if sc2 == 0:
    print("당신은 천재입니다!")
