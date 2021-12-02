# 21. 중복 문자 제거(★★★)

# ** 중복된 문자를 제외하고 사전식 순서로 나열하라.

# 예제 1 : 입력 = "bcabc", 출력 ="abc"
# 예제 2 : 입력 = "cbacdcbc", 출력 = "acdb"



# 방법 1. 재귀를 이용한 분리
def solution(self, s:str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + self.solution(suffix.replace(char,''))
    return ''

# 방법 2. 스택을 이용한 문자 제거
def solution(self, s:str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -=1
        if char in seen: # 이미 처리된 문자 여부를 확인하기 위해 사용
            continue
        
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    return ''.join(stack)
    