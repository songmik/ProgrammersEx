# 크레인 인형뽑기 게임 https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    basket =[] # 인형을 담아줄 basket

    for i in moves: # 사용자의 움직임을 하나씩 반복해봄
        for j in range(len(board)): 
            if board[j][i-1] == 0:  
                pass
            else:
                basket.append(board[j][i-1]) #basket에 인형 넣음
                board[j][i-1] = 0 
                break
        if len(basket) >=2:
            if basket[len(basket)-1] == basket[len(basket)-2]: # 길이가 2이상일 때
                basket.pop(-1) # 인형 제거 1개
                basket.pop(-1) # 인형 제거 1개
                answer += 2 # 인형 2개가 사라졌으니 answer에 2를 더해줌

    return answer 
