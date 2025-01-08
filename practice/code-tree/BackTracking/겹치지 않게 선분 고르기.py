# 겹치지 않게 선분 고르기
'''
n개의 선분, 겹치지 않게 가장 많은 수의 선분 고르기
끝점을 공유하는 것 역시 겹친 것으로 생각
-> 현재 선택하려고 하는 선분이 지금까지 고른 선분들과 겹치지 않는다면 선택
-> 기울기가 같으면 같은 직선으로 간주?
-> 모든 선분을 탐색하였다면 재귀 종료
'''
n = int(input())
x_pos,y_pos = [],[] # 각 선분의 좌표
for _ in range(n):
    x,y = map(int,input().split())
    x_pos.append(x)
    y_pos.append(y)

select = [] # 지금까지 선택된 선분의 집합

# 지금까지 선택한 좌표들과 현재 좌표가 겹치는지 검사
# 15 * 15 = 225 O(n^2) -> 최대 225
def is_collide(x,y):
    for lx,ly in select:
        if x<=lx<=y:
            return True
        if lx<=x<=ly:
            return True
        if lx<=y<ly:
            return True
    return False # 현재 좌표에 대해 충돌하지 않음

def dfs(depth, cnt):
    global result
    result = max(result,cnt)

    if depth == n: # 마지막 선분까지 모두 검사를 마쳤다면 -> 종료 조건
        return

    for i in range(depth, n):
        x,y = x_pos[i], y_pos[i]
        # 해당 선분을 선택했을때 기존 선분들과 충돌이 발생하지 않는다면
        if not is_collide(x,y):
            select.append((x,y))
            dfs(i+1, cnt+1)
            select.pop() # 백트래킹

result = 0
dfs(0,0)
print(result)