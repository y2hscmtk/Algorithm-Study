# https://www.acmicpc.net/problem/19942
'''
3 <= n <= 15
백트래킹, 브루트포스
'''
n = int(input())
limit = list(map(int,input().split())) # 단백질, 탄수화물, 지방, 비타민 최소치
data = [list(map(int,input().split())) for _ in range(n)]
select = [] # 조건을 만족하는 식재료 조합 찾기

# 현재 선택된 조합이 최소 비용 기준 만족하는지 확인
def is_possible():
    global min_cost
    # 각 선택된 영양소에 대해서
    check = [0,0,0,0,0]
    for i in range(len(select)):
        for j in range(len(data[select[i]])):
            check[j] += data[select[i]][j]
    # 모두 최소치를 만족하는지 확인
    for j in range(len(check)-1):
        if check[j] < limit[j]:
            return -1
    return check[-1]

array = []
def dfs(s,cnt):
    global min_cost,array
    # 현재 조합에서 조건 만족하는지 확인 필요
    cost = is_possible()
    if cost != -1:
        if min_cost > cost:
            min_cost = cost
            array = [s+1 for s in select]
    # 최대 n개까지 선택 가능
    if cnt == n:
        return
    for i in range(s,n):
        select.append(i)
        dfs(i+1,cnt+1)
        select.pop()

min_cost = float('inf')
dfs(0,0)
if array:
    print(min_cost)
    print(*array)
else:
    print(-1)
