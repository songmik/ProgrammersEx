# 16. 두 수의 덧셈

# ** 역순으로 저장된 연결 리스트의 숫자를 더하라.

# 예제 : 입력 = (2->4->3) + (5 -> 6-> 4) , 출력 = 7 -> 0-> 8 
# 설명 : 342+465=807



# 방법 1. 자료형 변환
class Solution:
    # 연결 리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # 파이썬 리스트를 연결 리스트로 변환
    def toReverseLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
        
        # 최종 계산 결과 연결 리스트 변환
        return self.toReverseLinkedList(str(resultStr))


# 방법 2. 전가산기 구현
def solution(self, l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        # 두 입력값의 합 계산
        if l1:
            sum +=l1.val
            l1 = l1.next
        if l2:
            sum +=l2.val
            l2 = l2.next

        # 몫(자리올림수)과 나머지(값) 계산
        carry, val = divmod(sum + carry, 10) # divmod() : 몫과 나머지로 구성된 튜플을 리턴. 
        head.next = ListNode(val)
        head = head.next

    return root.next