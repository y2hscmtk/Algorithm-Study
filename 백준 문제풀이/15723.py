# https://www.acmicpc.net/problem/15723
'''
문제
모든 중앙대 컴퓨터공학부(소프트웨어학부) 학생들은 미인이다.

지무근은 중앙대 컴퓨터공학부 학생이다.

그러므로 지무근은 미인이다.

위 연역 논증은 대표적인 삼단논법의 예시이다. 
삼단논법이란 전제 두 개와 결론 하나로 이루어진 연역 논증이다. 
이것을 응용하면, n개의 전제가 있을 때 m개의 결론을 도출할 수 있을 것이다. 
이때의 n과 m은 모든 의미에서 적절한 수라고 가정하자. 자세한 것은 입출력 예시를 확인하자.
'''
from collections import deque
dict = {}
for _ in range(int(input())):
    s = input()
    # 공백으로 구분 => is 분리
    s.split()
    dict[s[0]] = s[-1]  # dict['a'] = 'b'


# bfs정의
def bfs(start, end, visited):  # 시작 노드, 목적지 노드
    queue = deque()
    queue.append(start)
    while queue:
        n = queue.popleft()
        # 목적지에 도달했는지 확인
        if n == end:
            return "T"
        if n in dict:
            for node in dict[n]:
                # 아직 방문한적 없는 노드라면
                if node not in visited:  # 아직 방문한적 없는 노드라면
                    visited.append(node)  # 방문처리
                    queue.append(node)
    # 목적지에 도달하지 못했다면
    return "F"


# 탐색
for _ in range(int(input())):
    s = input()
    # 공백으로 구분 => is 분리
    s.split()
    visited = []  # 방문정보를 저장할 배열 초기화
    visited.append(s[0])  # 방문처리
    print(bfs(s[0], s[-1], visited))
