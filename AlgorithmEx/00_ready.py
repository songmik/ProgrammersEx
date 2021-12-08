"""
변수 : 프로그램에서 값을 저장하여 사용하거나 계산한 결과를 다시 보관하는 정보의 저장 공간
객체(Object) : 현실에 있는 물체, 또는 가상한 존재로, Class를 이용하여 프로그래밍에 옮겨 구현.
클래스(Class) : 클래스는 '틀'에 해당




- 데크 : 더블 엔디드 큐의 줄임말로, 글자 그대로 양쪽 끝을 모두 추출할 수 있는, 큐를 일반화한 형태의 추상 자료형임




"""

# 거북이 그래픽으로 도형 그리기
import turtle as t

# 삼각형
t.color("red")
t.forward(100)
t.left(120) # 왼쪽으로 120도 회전
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

# 사각형
t.color("green")
t.pensize(3) # 펜 굵기
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# 원
t.color("blue")
t.pensize(5)
t.circle(50) # 반지름이 50인 원



