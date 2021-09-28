# 2016년 https://programmers.co.kr/learn/courses/30/lessons/12901

# 가장 짧은 코드
import datetime

def solution(a,b):
    time = 'MON TUE WED THU FRI SAT SUN'.split()
    return time[datetime.datetime(2016,a,b).weekday()]

# datetime : 현재 날짜와 시간 구하기
# 참고 : https://dojang.io/mod/page/view.php?id=2463

