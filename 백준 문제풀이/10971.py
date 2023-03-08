# https://www.acmicpc.net/problem/10971
'''
각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. 

W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다. 

비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다. 

모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다. 

경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.
'''
from collections import deque
import sys

# 도시의 수
n = int(input())
# i도시에서 j도시로 이동하는데 필요한 비용은 w[i][j]로 표현
# i에서 j로 갈수 있는 경로가 없다면 0으로 표현
w = [list(map(int, input().split())) for _ in range(n)]

# 모든 도시를 순회하고 다시 원래 도시로 돌아오는데 필요한 최소비용 구하기
result = sys.maxsize

# 도시의 방문 정보를 기록
visited = [False]*n


# dfs정의 시작도시, 현재도시, 총 비용, 지금까지 방문한 도시 수
def dfs(start, now, price, count):
    global result
    # 만약 지금까지 방문한 도시 수가 전체 도시수가 됐다면 => 모든 도시를 방문했다면
    if count == n:
        # 마지막 도시에서 처음으로 되돌아오는 경로가 있는지 확인하고,
        # 해당 경로를 더해서 최소비용을 업데이트한다
        if w[now][start] != 0:  # 처음 도시로 되돌아오는 경로가 존재한다면
            # 되돌아오는데 필요한 비용을 더한값과 현재까지의 최소비용중 더 작은 값을 최소값으로 갱신
            result = min(result, price+w[now][start])
            return  # 함수 종료
    # 만약 모든 도시를 방문하기도 전에, 비용이 더 높아진다면 남은 도시를 방문할 필요 없음 => 시간초과 판정 방지
    if price > result:
        return  # 함수 종료

    for i in range(n):
        # 아직 해당 도시를 방문하지 않았고, 해당 도시로의 경로가 존재한다면
        if not visited[i] and w[now][i] != 0:
            visited[i] = True  # 방문처리
            # 시작 도시정보는 보관한채로, 현재 도시를 i로 변경, 비용 누적, 방문도시수 +1
            dfs(start, i, price+w[now][i], count+1)
            visited[i] = False  # 백트래킹 => 다시 방문하지 않은 처리


        # 탐색을 시작할 도시 선별
for i in range(n):
    # i번째 도시 방문처리
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(result)
