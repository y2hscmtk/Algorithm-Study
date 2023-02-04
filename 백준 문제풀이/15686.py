# https://www.acmicpc.net/problem/15686
'''
치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 
즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다.

프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 한다. 
오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개라는 사실을 알아내었다.

도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 
어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.
'''
'''
아이디어 : 탐색을 진행하며 치킨집의 위치를 배열에 기록해둔다.
이후 combination을 이용하여, 임의의 m개의 위치를 고른후 해당위치에 치킨집을 제거했을때의 치킨거리를 계산하고
모든 경우의 수에 대해 위 과정을 반복하며 치킨거리에 대한 최소값을 갱신하여 답을 구한다.
'''
from itertools import combinations
import sys
input = sys.stdin.readline

# 도시의 크기는 n*n, m은 제거할 치킨집의 수
n, m = map(int, input().split())
# 도시 정보 입력받기
city = [list(map(int, input().split())) for _ in range(n)]

# 치킨집의 위치를 저장할 배열
chickenShop = []
# 집의 위치를 저장할 배열
house = []
# 정답을 저장할 변수
result = sys.maxsize

# 0은 빈 칸, 1은 집, 2는 치킨집을 의미한다
# 도시를 탐색하여 치킨집 위치 기록
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickenShop.append([i, j])  # 치킨집 위치 기록
        elif city[i][j] == 1:
            house.append([i, j])

# 치킨집은 최소 1개 이상 남아있어야함
for i in range(1, m+1):
    temp = sys.maxsize  # 임시로 최단 치킨거리를 기록할 변수
    # i개 만큼의 치킨집만 유지시킨다.
    for chickenList in combinations(chickenShop, i):
        # 남아있는 치킨집을 대상으로 치킨거리 탐색
        cityDistance = 0  # 도시의 치킨거리
        for hx, hy in house:
            minDistance = sys.maxsize  # 최소거리를 저장할 변수
            for cx, cy in chickenList:
                # 가장 가까운 치킨거리 탐색
                minDistance = min(minDistance, (abs(hx-cx)+abs(hy-cy)))
            cityDistance += minDistance  # 치킨거리 저장
        temp = min(temp, cityDistance)

    result = min(result, temp)

print(result)
