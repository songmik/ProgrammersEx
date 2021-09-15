# 모의고사 https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer =[]
    count = [0,0,0] # 수포자가 맞은 수를 기록하는 배열
    person1 = [1,2,3,4,5] # 수포자1 (5주기)
    person2 = [2,1,2,3,2,4,2,5] # 수포자2 (8주기)
    person3 = [3,3,1,1,2,2,4,4,5,5] # 수포자3 (10주기)

    for i in range(len(answers)):
        if answers[i] == person1[i%5]: # 수포자1은 5 주기로 반복
            count[0] += 1
        if answers[i] == person2[i%8]: # 수포자2은 8 주기로 반복
            count[1] += 1
        if answers[i] == person3[i%10]: # 수포자3은 10 주기로 반복
            count[2] += 1

    max_1 = max(count) # 가장 많이 맞춘 수

    for i in range(3): # 가장 많이 맞춘 사람을 배열에 담기
        if max_1 == count[i]:
            answer.append(i+1)

    return answer
