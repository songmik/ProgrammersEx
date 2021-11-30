# 20. 유효한 괄호(★)

# ** 괄호로 된 입력값이 올바른지 판별하라.

# 예제 : 입력 = ()[]{}, 출력 = true



# 방법 : 스택 일치 여부 판별
def solution(self, s: str) -> bool:
    stack =[]
    table = {
        ')':'(', # ([{ -> 스택에 푸시, }]) -> 를 만나면 스택에서 pop함
        '}':'{',
        '[':']',
    }

    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in s:
        if char not in table: # 매핑 테이블을 만들어 놓고 테이블에 존재하지 않으면 푸쉬
            stack.append(char)
        elif not stack or table[char] != stack.pop(): # 팝했을 때 결과가 일치하지 않으면 False를 리턴
            return False
    return len(stack) == 0