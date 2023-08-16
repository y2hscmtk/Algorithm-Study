# https://www.acmicpc.net/problem/26215
'''
무조건 2집씩 청소하는게 이득
내림차순 정렬 후, 앞에서부터 2개씩 선택해서 1씩 깎기
모두 0이 되면 그만두기
'''
import sys
n = int(input())
snow = list(map(int, input().split()))

# 모든 집이 청소가 완료됐는지 검사


def check():
    for i in range(n):
        if snow[i] != 0:
            return False
    return True  # 모두 청소됐다면


time = 0  # 걸린 시간
if n == 1:  # 집이 한곳만 있을수도
    if snow[0] > 1440:
        print(-1)
    else:
        print(snow[0])
    sys.exit(0)
while True:
    snow.sort(reverse=True)  # 앞에서 부터 눈이 가장 많이 내린 두 집 선택
    # 모든 집이 청소가 완료됐다면 종료
    if check():  # 모두 청소됐다면
        break  # 종료
    # 모두 청소되지 않았다면
    # 두 집을 선택 0,1 => 1번 집이 0일 수도 있으니 확인
    if snow[1] == 0:
        # 0번 집을 청소하고, 그만큼 시간 더하기
        time += snow[0]
        snow[0] = 0
    else:  # 선택 가능한 두 집이 남아있는경우 => sort를 했기 떄문에 0,1에는 항상 눈이 쌓여 있을 것
        snow[0] -= 1
        snow[1] -= 1
        time += 1
    # 시간이 1440초를 초과했는지 검사
    if time > 1440:
        print(-1)
        sys.exit(0)
print(time)
