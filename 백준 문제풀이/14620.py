# https://www.acmicpc.net/problem/14620
'''
(1,1) ~ (n-2,n-2)의 영역에서 꽃 심기 가능
점을 3개 고르고, 3개 골랐으면 꽃을 심을 수 있는지 검사
심을 수 있다면 최소가격 최신화
'''
import sys
n = int(input())
flower = [list(map(int, input().split())) for _ in range(n)]
result = sys.maxsize
selected = []


def select_map(count):
    global selected
    # 만약 땅을 3개 선
    if count == 3:  # 3개 선택했다면
        check_and_update()  # 선택한 땅에 꽃을 심어도 모두 사는지 확인후, 가격 업데이트
    else:
        for i in range(1, n-1):
            for j in range(1, n-1):
                if (i, j) not in selected:
                    selected.append((i, j))  # 땅 선택
                    select_map(count+1)
                    selected.pop()  # 땅 선택 취소


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def check_and_update():
    global result
    grow = []  # 꽃이 자라게 될 위치
    for x, y in selected:
        # 꽃을 심은 땅 grow에 삽입
        grow.append((x, y))
        # 해당 땅의 상하좌우 좌표 검사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 영역을 벗어나지 않는지
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                return
            if (nx, ny) in grow:  # 꽃이 모두 살아남을 수 있는지(겹치지 않는지)
                return
            grow.append((nx, ny))
    # 모두 살아남았다면 가격 업데이트
    cost = 0
    for (x, y) in grow:
        cost += flower[x][y]
    result = min(result, cost)


select_map(0)
print(result)
