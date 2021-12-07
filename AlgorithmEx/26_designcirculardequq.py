# 26. 원형 데크 디자인(★★)

# ** 다음 연산을 제공하는 우넌형 데크를 디자인하라.

"""
- MyCircularDeque(k) : 데크 사이즈를 k로 지정하는 생성자다.
- insertFront() : 데크 처음에 아이템을 추가하고 성공할 경우 true를 리턴한다.
- insertLast() : 데크 마지막에 아이템을 추가하고 성공할 경우 true를 리턴한다.
- deleteFront() : 데크 처음에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
- deleteLast() : 데크 마지막에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
- getFront() : 데크 첫 번째 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
- getLast() : 데크 마지막 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
- isEmpty() : 데크가 비어 있는지 여부를 판별한다.
- isFull() : 데크가 가득 차 있는지 여부를 판별한다.
"""


# 방법 : 이중 연결 리스트를 이용한 테크 구현
class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len +=1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -=1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -=1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getReat(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k