# https://www.acmicpc.net/problem/1051
'''
브루투포스, 구현
'''
n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

result = 1  # 최대 넓이를 기록하기 위함 => 모두 일치하지 않는다면 숫자 한개가 가장 큰 정사각형


# x,y 타겟 숫자의 왼쪽 위 좌표
# target 타겟 숫자
def find(y, x, target):
    global result
    # 정사각형을 만족하면서 각 꼭짓점의 숫자가 모두 같으면 됨
    # 1부터, 가로로 남은 영역만큼(최대 가로 길이) 길이를 늘려가면서 확인
    for length in range(1, m-x):  # 1 ..m-x까지 예를 들어 현재 좌표가 (1,3)이고 가로가 5까지 있을때 => 1,2까지 가능
        # length는 정사각형으로 가능한 한 변의 길이를 의미
        # length를 y 좌표에 넣었을때 영역을 벗어나지 않는지(정사각형을 만들 수 있는지 확인)
        if length + y >= n:  # 영역을 벗어난다면 함수종료
            return
        # 영역을 벗어나지 않는다면(정사각형을 만들 수 있다면)
        # 모든 사각형의 꼭짓점이 다 같은지 확인
        if data[y][x] == data[y+length][x] and data[y][x] == data[y][x+length] and data[y][x] == data[y+length][x+length]:
            # 만들어질수있는 정사각형의 최대 넓이 업데이트
            result = max(result, (length+1)*(length+1))


for i in range(n):
    for j in range(m):
        target = data[i][j]  # 정사각형을 탐색할 타겟 숫자 지정
        # 해당 숫자를 기준으로 정사각형 탐색 시작
        find(i, j, target)

print(result)
