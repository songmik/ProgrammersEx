# 4. 가장 흔한 단어(★)

# ** 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.

# 예제 1. 입력 paragraph = "Bob hit a ball, the hit BALL flew far after it was hit" , banned = ["hit"]
#         출력 = "ball"



# 방법 : 리스트 컴프리헨션, Counter 객체 사용
def solution(self, paragraph: str, banned: List[str]) -> str:
    # \w = 단어 문자, ^ = not 을 의미 => 모든 문자를 공백으로 치환
    # words에는 소문자, 구두점, bannded를 제외한 단어 목록이 저장됨
    words = [word for word in re.sub(r'[^\w]',' ', paragraph).lower().split() if word not in banned]

    # 가장 많이 등장하는 단어를 셈
    counts = collections.Counter(words)

    # words에서 가장 흔하게 등장하는 단어의 첫 번째 값을 most_common(1)으로 추출=> [('ball', 2)] 에서 [0][0]인 'ball'이 가장 흔한 단어가 된다.
    return counts.most_commoon(1)[0][0]