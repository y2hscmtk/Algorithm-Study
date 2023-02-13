# https://www.acmicpc.net/problem/1005
'''
특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램을 작성해주자.

첫째 줄에는 테스트케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 주어진다. 

첫째 줄에 건물의 개수 N과 건물간의 건설순서 규칙의 총 개수 K이 주어진다. (건물의 번호는 1번부터 N번까지 존재한다) 

둘째 줄에는 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN이 공백을 사이로 주어진다. 

셋째 줄부터 K+2줄까지 건설순서 X Y가 주어진다. (이는 건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미이다) 

마지막 줄에는 백준이가 승리하기 위해 건설해야 할 건물의 번호 W가 주어진다.
'''
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    # 건물의 개수 n개, 건물간 건설 규칙의 순서
    n, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]  # 건설 규칙의 순서를 기록하기 위함
    build = [False for _ in range(n+1)]  # 건물을 다 지었는지를 체크하기 위함
    # 각 건물을 짓는데 걸리는 시각(cost) 기록
    cost = list(map(int, input().split()))
    # 각 건물을 짓기 위한 요구사항을 기록하기 위한 배열
    require = [[] for _ in range(n+1)]
    for j in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)  # 건물 x를 지은후 y를 지을수 있음을 의미
        require[y].append(x)  # 건물 y를 짓기 위해서 x를 먼저 지어야됨을 의미
    w = int(input())  # 승리를 위해 지어야하는 건물 w
