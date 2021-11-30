# 17. 페어의 노드 스왑(★★)

# ** 연결 리스트를 입력받아 페어 단위로 스왑하라.

# 예제 : 입력 = 1->2->3->4 , 출력 = 2->1->4->3



# 방법 1. 값만 교환
def solution(self, head:ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head


# 방법 2. 반복 구조로 스왑 -> head를 가리키는 노드가 직접 바뀌는 풀이
def solution(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        # b가 a(head)를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next

    return root.next


# 방법 3. 재귀 구조로 스왑 -> 불필요한 변수를 사용하지 않아 공간 복잡도가 낮으면서, 빈틈 없는 구조를 지니고 있음
def solution(self, head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next # 포인터 역할을 하는 p변수
        # 스왑된 값 리턴 받음
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head

