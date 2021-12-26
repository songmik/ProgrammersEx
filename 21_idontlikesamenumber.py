# 같은 숫자는 싫어 https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer=[] # 원소를 담을 리스트 'answer'
    answer.append(arr[0]) # arr[0]에 있는 원소를 answer에 더해줌
    for i in range(1, len(arr)): # 1~ len(arr) 까지 반복
        if arr[i-1] != arr[i]: # i 와 i-1의 원소가 다른지 비교
            answer.append(arr[i]) # 다르면 answer 리스트에 추가
    return answer
