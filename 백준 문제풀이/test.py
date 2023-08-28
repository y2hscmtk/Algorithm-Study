data = [list(map(int, input().split())) for _ in range(9)]
x, y, max_num = 0, 0, data[0][0]
for i in range(9):
    for j in range(9):
        if data[i][j] > max_num:
            x, y, max_num = i, j, data[i][j]
print(max_num)
print(i+1, j+1)
