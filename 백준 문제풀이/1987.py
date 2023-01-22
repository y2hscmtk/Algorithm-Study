# https://www.acmicpc.net/problem/1987

'''
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 

보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 

좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 

새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 

달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.
'''
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().strip()) for i in range(r)]

# 방향벡터 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0
# 시간복잡도문제를 해결하기위해 아스키코드로 변환하여
# 알파벳의 번호를 직접 방문처리
visited = [False] * 26

# 이전에 지나온 알파벳을 다시 가지 않아야함
# 지나온 알파벳에 대한 정보를 기록해서 누적시켜야함
# 네 방향에 대해 dfs를 수행하며 더 길이가 긴 경우를 출력한다.
def dfs(x, y, count):
    global result

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < r and 0 <= my < c:
            # 아직 방문한적 없는 알파벳이면 방문
            # 아스키코드로 변환하여 확인 A : 0번 B : 1번 ...
            if not visited[ord(graph[mx][my])-65]:
                # copy_visited = copy.deepcopy(visited)
                visited[ord(graph[mx][my])-65] = True  # 방문처리
                dfs(mx, my, count+1)  # 방문처리된상태로 탐색
                visited[ord(graph[mx][my])-65] = False  # 방문해제(백트래킹)
    # 길이가 더 긴지 검사하여 누적시키고, 탐색 종료
    result = max(result, count)


visited[ord(graph[0][0])-65] = True
dfs(0, 0, 1)
print(result)
