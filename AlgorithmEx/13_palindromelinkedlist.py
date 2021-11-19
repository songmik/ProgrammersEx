# 13. 팰린드롬 연결 리스트(★)

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
    - Node : 데이터와 다음 데이터를 가리키는 주소로 이루어짐

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

"""
 데크 : 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형으로 스택처럼 써도 되고 큐처럼 써도 된다
  - collections.deque 모듈은 자료형을 생성하는 모듈
  - 참고 : https://wikidocs.net/104977

"""


# 방법 3. 런너를 이용한 우아한 풀이
def solution(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head # head에서 시작

    # 런너를 이용해 역순 연결 리스트 구성 -> next가 존재하지 않을 때까지 이동
    while fast and fast.next:
        fast = fast.next.next  # fast 런너는 두 칸씩 이동 , slow 한 칸씩 이동
        rev, rev.next, slow = slow, rev, slow.next  # 역순 연결 리스트 : 현재 값을 slow로 교체하고 rev.next는 rev가 됨 => 앞에 계속 새로운 노드가 추가되는 형태
    if fast: # 홀수와 짝수일 때 마지막 처리가 다르기 때문에, 홀수일 때 slow 런너가 한 칸 더 앞으로 이동하여 중앙의 값을 빗겨 나가야 함
        slow - slow.next # fast가 None이 아니라는 경우로 간주할 수 있기 때문에 slow를 한 칸 더 이동해 마무리함

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val: 
        slow, rev = slow.next, rev.next
    return not rev # return not slow를 해도 똑같은 결과

"""
 런너 : 연결 리스트 순회 시 2개의 포인터를 동시에 사용하는 기법
  - 빠른 런너와 느린 런너를 각각 출발시키면, 빠른 런너가 끝에 다다를 때 느린 런너는 정확히 중간 지점에 도달하게 된다.
"""