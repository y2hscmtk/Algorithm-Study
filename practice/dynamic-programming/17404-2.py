# https://www.acmicpc.net/problem/17404
'''
Top-down 기법 풀이
'''
import sys
sys.setrecursionlimit(1001)

INF = float('inf')

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

def paint_cost(house, color, first_color):
    if house == n - 1: # 마지막 집에 도달한 경우
        # 마지막 집은 첫 번째 집과 같은 색을 칠할 수 없음
        return cost[house][color] if color != first_color else INF
    
    # 이미 계산된 경우 반환
    if memo[house][color] != INF:
        return memo[house][color]
    
    # 현재 집을 color로 칠할 때의 최소 비용 계산
    result = INF
    for next_color in range(3):
        if next_color != color:  # 인접한 집은 같은 색이 될 수 없음
            result = min(result, paint_cost(house + 1, next_color, first_color))
    
    # 현재 집의 최소 코스트 반환
    memo[house][color] = result + cost[house][color]
    return memo[house][color]

# 모든 경우의 최소 비용 계산
min_cost = INF
for first_color in range(3):
    # 메모이제이션 테이블 초기화
    memo = [[INF] * 3 for _ in range(n)]
    # 첫 번째 집의 색상을 고정하고 최소 비용 계산
    min_cost = min(min_cost, paint_cost(0, first_color, first_color))

print(min_cost)
