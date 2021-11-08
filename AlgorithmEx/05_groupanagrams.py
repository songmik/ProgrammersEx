# 5. 그룹 애너그램(★★) : 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것, ex) 문전박대 -> 대박전문 

# ** 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

# 예제 1. 입력 = ["eat", "tea", "tan", "ate", "nat", "bat"]
#         출력 = [
#                   ["ate","eat", "tea"],
#                   ["nat", "tan"],
#                   ["bat"]
#                 ]



# 방법 : 정렬하여 딕셔너리에 추가하는 방법
def solution(self, strs: List[str]) -> List[List[str]]:
    # 존재하지 않는 키를 삽입하려할 경우 KeyError가 발생하므로 에러가 나지 않도록 디폴트를 생성해주는 defaultdict()로 선언
    anagrams = collections.defaultdict(list)

    for word in strs:
        # sorted()는 문자열을 정렬하여 결과를 리스트로 리턴하기 때문에 join()으로 합쳐서 딕셔너리로 구성함
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

""" &&& sort()와 sorted()의 차이점 &&&

1. sort() : 매서드를 사용해 리스트의 요소를 작은 순서대로 정렬(오름차순) -> 원래 변수가 수정되는 것
 - a = [10,20,30,15,20,40] (a의 내용을 변경하여 정렬)
 - a.sort() = [10,15,20,20,30,40]

2. sorted() : 정렬된 새 리스트를 생성함 -> 원래 변수는 수정되지 않음
 - a = [10,20,30,15,20,40]
 - sorted(a) = [10,15,20,20,30,40]

"""