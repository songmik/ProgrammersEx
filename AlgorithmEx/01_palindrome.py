# 1. 팰린드롬 : 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장.

# ** 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다. **

# 예제 1. 입력 = "A man, a plan, a canal: Panama" , 출력 : true
# 예제 2. 입력 = "race a car" , 출력 : false



# 방법 1 . 리스트로 변환하는 방법
def solution(self, s:str) -> bool:
    str=[]
    for i in s:
        if i.isalnum():
            str.append(i.lower())

    # 팰린드롬 여부 판별
    while len(str) > 1:
        if str.pop(0) != str.pop():
            return False

    return True


# 방법 2. 슬라이싱 사용
def solution(self, s:str) -> bool:
    s = s.lower()

    # 불필요한 문자 필터링
    # re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
    # 참고 ( re.sub : https://dojang.io/mod/page/view.php?id=2438 )
    s = re.sub('[^a-z0-9]','',s) 

    return s == s[::-1] # 슬라이싱 -> 문자를 뒤집음
    # ex) 안녕하세요 -> s[::1] = 안녕하세요 , s[::-1] = 요세하녕안 
