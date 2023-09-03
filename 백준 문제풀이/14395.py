# https://www.acmicpc.net/problem/14395
'''
정수 s가 주어진다. 정수 s의 값을 t로 바꾸는 최소 연산 횟수를 구하는 프로그램을 작성하시오.

사용할 수 있는 연산은 아래와 같다.

s = s + s; (출력: +)
s = s - s; (출력: -)
s = s * s; (출력: *)
s = s / s; (출력: /) (s가 0이 아닐때만 사용 가능)

s와 t가 같은 경우에는 0을, 바꿀 수 없는 경우에는 -1을 출력
가능한 방법이 여러 가지라면, 사전 순으로 앞서는 것을 출력
연산의 아스키 코드 순서는 '*', '+', '-', '/' 이다.
'''
from collections import deque
INF = int(10**9)


def bfs():
    visited = set()
    queue = deque()
    queue.append([s, ""])
    while queue:
        x, result = queue.popleft()
        # 찾고자 하는 수 발견시
        if x == t:
            return result
        # *연산의 경우
        if (x*x) <= INF and (x*x) not in visited:
            queue.append([x*x, result+"*"])
            visited.add(x*x)  # 방문처리
        # +연산의 경우
        if (x+x) <= INF and (x+x) not in visited:
            queue.append([x+x, result+"+"])
            visited.add(x+x)  # 방문처리
        # -연산의 경우 => 빼면 무조건 0 (서로 같은 수)
        if 0 not in visited:
            queue.append([0, result+"-"])
            visited.add(0)  # 방문처리
        # /연산의 경우 => 나누면 무조건 1(서로 같은 수)
        if x != 0 and 1 not in visited:
            queue.append([1, result+"/"])
            visited.add(1)  # 방문처리
    return -1  # bfs에서 찾지 못했을 경우


s, t = map(int, input().split())
if s == t:
    print(0)
else:
    print(bfs())
