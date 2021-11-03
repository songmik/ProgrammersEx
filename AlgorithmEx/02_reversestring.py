# 2. 문자열 뒤집기

# ** 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내붑를 직접 조작하라.

# 예제 1. 입력 : ["h", "e", "l", "l", "o"] , 출력 : ["o", "l", "l", "e", "h"]
# 예제 2. 입력 : ["H", "a", "n", "n", "a", "H"] , 출력 : ["h","a", "n", "n", "a", "H"] 



# 방법 1. 투 포인터를 사용하는 방법 : 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식, s 내부를 스왑하는 형태로 풀이
def solution(self, s:List[str]) -> None:
    left, right = 0, len(s) -1
    while left < right: 
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# 방법 2. reverse() 함수를 사용해 뒤집는 방법
def solution(self, s: List[str]) -> None:
    s.reverse() # 입력값이 리스트로 제공되므로, 리스트를 뒤집을 수 있는 reverse()함수를 이용한다 !