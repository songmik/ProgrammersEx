# 키패드 누르기 https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    Left = 10 # 키패드 '*'을 10으로 정의
    Right = 12 # 키패드 '#'을 12로 정의
    
    for n in numbers:
        if n in [1,4,7]: # 키패드의 왼쪽 줄에 있는 1,4,7 -> 왼손으로 입력
            answer+='L'
            Left = n
        elif n in [3,6,9]: # 키패드의 오른쪽 줄에 있는 3,6,9 -> 오른손으로 입력
            answer+='R'
            Right = n
        else: # 키패드 가운데에 있는 경우 -> 왼손, 오른손의 거리 계산
            n = 11 if n == 0 else n
            
            Left2 = abs(n-Left) 
            Right2 = abs(n-Right)
            
            if sum(divmod(Left2, 3)) > sum(divmod(Right2, 3)): # 오른손의 거리가 더 짧다 -> 오른손으로 입력
                answer+='R'
                Right = n
            elif sum(divmod(Left2, 3)) < sum(divmod(Right2, 3)): # 왼손의 거리가 더 짧다 -> 왼손으로 입력
                answer +='L'
                Left = n
            else: # 왼손과 오른손의 거리가 같을 때 -> 값에 따라 입력
                if hand == 'left':
                    answer+='L'
                    Left = n
                else:
                    answer+='R'
                    Right = n
                
    return answer

