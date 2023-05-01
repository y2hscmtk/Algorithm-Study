# https://www.acmicpc.net/problem/2630
n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

count = [0, 0]  # 흰색종이, 파란색종이


# 분할정복
def cut(s_x, s_y, size):
    color = data[s_x][s_y]
    # 색종이의 크기가 1x1이라면 종료
    if size == 1:
        # 해당 색종이 색의 개수를 늘리고 종료
        count[color] += 1
        return
    # 모든 색종이의 색이 같다면 자를필요 없이 종료
    error = False
    for i in range(s_x, s_x+size):
        for j in range(s_y, s_y+size):
            if data[i][j] != color:
                error = True
                break
        if error:
            break
    if not error:
        count[color] += 1  # 에러가 없다 => 모든색이 일치한다 => 개수증가
        return
    # 리턴을 하지 못했다면 에러가 있었다는 의미, 즉 색이 다른 색종이가 있었다
    size //= 2
    cut(s_x, s_y, size)
    cut(s_x, s_y+size, size)
    cut(s_x+size, s_y,  size)
    cut(s_x+size, s_y+size, size)


cut(0, 0, n)
# 정답 출력
print(count[0])
print(count[1])
