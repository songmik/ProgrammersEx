# 22. 일일 온도

# ** 매일의 화씨 온도 (F)리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라.

# 예제 : 입력 = T = [73,74,75,71,69,72,76,73] / 출력 = [1,1,4,2,1,1,0,0]



# 방법 : 스택 값 비교
def solution(self, T:List[int]) -> List[int]:
    answer =[0] * len(T)
    stack =[]
    for i, cur in enumerate(T):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer