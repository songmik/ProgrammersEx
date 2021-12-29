# Chapter 05. DFS/BFS


# 5-1. 스택 예제
stack = []

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])



# 5-2. 큐 예제
from collections import deque

queue = deque()

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse() # 역순으로 바꾸기
print(queue)



# 5-3. 재귀 함수 예제
def function():
    print('재귀 함수를 호출합니다.')
    function()

function() # '재귀 함수를 호출합니다.' 가 무한히 출력


# 5-4. 재귀 함수 종료 예제
def function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

function(1)



# 5-5. 2가지 방식으로 구현한 팩토리얼 예제
# 반복적으로 구현한 n!
def iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def recursive(n):
    if n <= 1:
        return 1
    # n! = n*(n-1)!를 그대로 코드로 작성하기
    return n * recursive(n-1)

#    => 둘 다 결과는 똑같음



# 5-6. 인접 행렬 방식
INF = 99999999

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]



# 5-7. 인접 리스트 방식 
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)



# 5-8. DFS 
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

            graph = [
                [],
                [2,3,8],
                [1,7],
                [1,4,5],
                [3,5],
                [3,4],
                [7],
                [2,6,8],
                [1,7]
            ]

            visited = [False] * 9
            dfs(graph, 1, visited)