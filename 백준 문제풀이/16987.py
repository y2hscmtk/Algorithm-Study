# https://www.acmicpc.net/problem/16987
'''
각 계란에는 내구도/무게가 존재 
계란 A와 계란 B를 부딛히면, 상대 계란의 무게만큼 현재 계란의 내구도가 까인다.
내구도가 0이하가 되면 계란은 깨진다.

각 계란에 대한 내구도/무게가 주어지며, 계란의 순서는 바꿀 수 없고 왼쪽부터 오른쪽까지 계란을 선택한다.
선택한 계란으로 다른 계란과 부딛힌다.

1. 가장 왼쪽 계란을 든다.
2. 다른 계란과 부딛힌다. 손에 든 계란이 부서졌거나 멀쩡한 계란이 남아있지 않으면 넘어간다.
3. 가장 최근에 든 계란의 바로 오른쪽 계란을 들어 2번 과정을 수행한다. 단, 가장 최근에 든 계란이 가장 오른쪽의 계란이라면 종료

최대 몇개의 계란을 깰 수 있을지 맞춰보자
'''
N = int(input())
# 내구도, 무게
egg = [list(map(int,input().split())) for _ in range(N)]

max_count = 0 # 최대로 깰 수 있는 달걀의 수

# 깨진 달걀 수 카운트
def count_crash_egg():
    return sum(1 for i in range(N) if egg[i][0] <= 0)


def dfs(idx):
    global max_count
    # 모든 달걀을 깨뜨릴수 있는 상황 발견시 더이상 시도할 필요 없음
    if max_count == N:
        return
    # 현재 깨진 계란 개수 갱신
    max_count = max(max_count, count_crash_egg())
    
    if idx == N:
        return
    
    # 현재 계란이 이미 깨졌으면 다음 계란으로 이동
    if egg[idx][0] <= 0:
        dfs(idx + 1)
        return
    
    # 왼쪽 달걀부터 가장 오른쪽 달걀까지 과정 수행
    # 다른 계란과 충돌 시도
    has_hit = False
    for target in range(N):
        # 자기 자신이 아니고, 대상 계란이 깨지지 않았다면 충돌
        if target != idx and egg[target][0] > 0:
            has_hit = True
            # 계란 충돌
            egg[idx][0] -= egg[target][1]
            egg[target][0] -= egg[idx][1]

            dfs(idx+1)

            # 계란 상태 복원
            egg[idx][0] += egg[target][1]
            egg[target][0] += egg[idx][1]
    
    # 충돌 가능한 계란이 없으면 다음으로 이동
    if not has_hit:
        dfs(idx + 1)

dfs(0)
print(max_count)
