# 가장 긴 팰린드롬 부분 문자열

# ** 가장 긴 팰린드롬 부분 문자열을 출력하라

# 예제 1. 입력 = "babad", 출력 = "bab" (or aba)
# 예제 2. 입력 = "cbbd" , 출력 = "bb"



# 방법. 중앙을 중심으로 확장하는 풀이
def solution(self, s : str) -> str:

    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left : int, right : int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # 해당 사항이 없을 때 빠르게 리턴하도록 예외 처리를 해줌
    if len(s) < 2 or s == s[::-1]:
        return s

    retult = ''

    # 슬라이딩 윈도우 우측으로 이동 -> 길이에서 -1 함
    for i in range(len(s) - 1):
        # 투 포인터가 점점 확장 -> i+1, i+2 
        retult = max(retult, expand(i, i+1),expand(i, i+2), key=len)
    return retult