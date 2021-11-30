# 18. 홀짝 연결 리스트(★★)

# ** 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.

# 예제 1. 입력 = 1->2->3->4->5->NULL, 출력 = 1->3->5->2->4->NULL
# 예제 2. 입력 = 2->1->3->5->6->4->7->NULL, 출력 = 2->3->6->7->1->5->4->NULL



# 방법 . 반복 구조로 홀짝 노드 처리
def solution(self, head: ListNode) -> ListNode:
    # 예외 처리
    if head is None:
        return None

    odd = head # 홀수 노드
    even = head.next # 짝수 노드
    even_head = head.next # 짝수 노드의 head(even_head) = head.next

    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next 
        odd, even = odd.next, even.next

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head # even_head (짝수 헤드)
    return head # head를 return 하면 head는 1, even_head는 2가 되기 때문에 조건을 충족
