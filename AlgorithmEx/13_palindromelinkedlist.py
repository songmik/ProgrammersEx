# 팰린드롬 연결 리스트

# ** 연결 리스트가 팰린드롬 구조인지 판별하라

# 예제 1. 입력 : 1 -> 2 , 출력 : false
# 예제 2. 입력 : 1 -> 2 -> 2 -> 1 , 출력 : true



# 방법1. 리스트 변환 (팰린드롬 여부를 판별하기 위해서는 앞,뒤로 모두 추출할 수 있는 자료구조가 필요)
def solution(self,head: ListNode) -> bool:
    q: List =[]

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True

"""
 연결 리스트
    - 데이터 요소의 선형 집합으로, 대표적인 선형 자료구조 중 하나로 다양한 추상 자료형 구현의 기반이 됨
    - 장점 : 새로운 노드를 삽입하거나 삭제하기가 간편


"""


# 방법 2. 데크를 이용한 최적화
def solution(self, head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) >1:
        if q.popleft() != q.pop():
            return False
    
    return True


# 방법 3. 런너를 이용한 우아한 풀이
def solution(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow - slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev