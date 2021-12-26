# 체육복 https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    reserve_1 = set(reserve)-set(lost) # 여벌이 있던 학생 중 잃어버린 학생을 뺌 -> 빌려줄 수 있는 학생
    lost_1 = set(lost) - set(reserve) # 여벌이 없는 학생 -> 참가 불가능 한 학생
    for i in reserve_1 : # 체육복을 빌릴 앞 뒤 사람을 찾음
        if i-1 in lost_1: # 앞사람
            lost_1.remove(i-1) 
        elif i+1 in lost_1: # 뒷사람
            lost_1.remove(i+1)
    answer = n-len(lost_1)
    return answer