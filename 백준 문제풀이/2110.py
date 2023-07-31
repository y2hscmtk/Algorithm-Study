# https://www.acmicpc.net/problem/2110
'''
두 공유기 사이의 거리를 mid로 두고 이분탐색 진행
모든 공유기는 각각 mid거리 이상의 거리를 두고 설치되어야함
=> 그래야 가장 인접한 최대거리가 mid가 나올 수 있을테니 
'''
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
house = [int(input().strip()) for _ in range(n)]
house.sort()  # 이분 탐색을 위해 집 위치 정렬
# 최소 거리는 0번~1번 집 사이, 최대 거리는 0번~-1번 집사이(끝과 끝)
# 가장 인접한 최대거리 집 => 결국 첫번째 집에는 무조건 설치해야 함
start = 1
end = house[-1]-house[0]
result = 1  # 인접거리 최소인 경우
while start <= end:
    mid = (start+end)//2

    last = house[0]  # 첫번째 집에는 무조건 공유기를 설치하고 들어감
    count = 1  # 1개는 무조건 설치됨
    # mid거리 이상에 공유기를 몇개 설치할 수 있는지 카운팅
    for i in range(1, n):
        # 지난 공유기와의 거리가 mid만큼 차이나면서 설치가 가능하다면
        if house[i] - last >= mid:
            count += 1  # 설치하고
            last = house[i]  # 이전 공유기 위치 갱신
            # count가 c개 이상 설치하는데 성공했는지 확인
            if count == c:
                break
    # 공유기의 개수 확인
    if count >= c:  # 설치하려던거보다 더 많이 설치한 경우
        # mid = 3일때 공유기 3개 이상 설치하는데 성공
        # 1 2 3 4 5 6 7 8
        # 0     0     0
        # => mid를 더 넓힐수 있는지 확인해야함
        start = mid + 1  # 오른쪽 영역으로 이동
        result = mid  # mid일때 c개 이상 설치임
    else:  # count < c
        # mid = 5일때 공유기 3개 이상 설치하는데 실패
        # 1 2 3 4 5 6 7 8
        # 0         0
        # => mid를 줄여서 다시 확인
        end = mid - 1  # 왼쪽 영역으로 이동
print(result)
