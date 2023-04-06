# https://www.acmicpc.net/problem/2980
n, l = map(int, input().split())

p = 0  # 현재 위치
time = 0  # 경과한 시간

for i in range(n):
    # 신호등 위치, 빨간색, 초록색 지속시간
    d, r, g = map(int, input().split())

    # 신호등이 있는곳 전까지 움직이는데 걸린 시간
    time += (d-p)
    p = d  # 신호등까지 이동
    # 현재 시간을 기준으로 신호등 색 계산
    # 현재시간에서 빨간불 + 초록불 총 경과시간을 나눈 나머지가
    # 빨간불 경과시간보다 작다면 => 즉 빨간불 진행중이라면
    if time % (r+g) <= r:
        time += (r-time % (r+g))  # 빨간시간 대기시간 만큼 더해주기

# 마지막 신호등으로부터 목적지까지 이동하는데 걸린 시간 더해주기
time += (l-p)
print(time)
