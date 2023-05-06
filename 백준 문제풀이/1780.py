# https://www.acmicpc.net/problem/1780

# 색종이 자르기랑 똑같은듯

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

count = [0, 0, 0]  # 0,1,-1 순으로


def cut(x, y, size):
    color = data[x][y]
    # 크기가 1인지(더이상 자를수 없는지 확인)
    if size == 1:
        count[color] += 1  # 해당 종류의 색종이 개수 증가
        return
    # 모두 같은 종류의 색종이인지 검사
    error = False
    for i in range(x, x+size):
        for j in range(y, y+size):
            if data[i][j] != color:  # 하나라도 종류가 다른 색종이가 있다면
                error = True
                break
        if error:
            break
    # 에러가 없다면 해당 종류의 색종이 카운트 증가
    if not error:
        count[color] += 1
        return
    # 리턴하지 못했다면 => 색이 다른 색종이 => 9등분 해야함
    size //= 3
    cut(x, y, size)
    cut(x+size, y, size)
    cut(x+2*size, y, size)
    cut(x+2*size, y+size, size)
    cut(x, y+size, size)
    cut(x, y+2*size, size)
    cut(x+size, y+2*size, size)
    cut(x+size, y+size, size)
    cut(x+2*size, y+2*size, size)


cut(0, 0, n)

# 정답 출력
print(count[-1])
print(count[0])
print(count[1])
