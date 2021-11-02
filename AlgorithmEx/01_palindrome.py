# 팰린드롬 : 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장.

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
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1]
