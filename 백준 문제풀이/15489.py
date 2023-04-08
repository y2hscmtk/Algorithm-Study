# https://www.acmicpc.net/problem/15489

# 이것도 미리 만들어두기?
r, c, w = map(int, input().split())

# r+w-1 층 까지의 파스칼 삼각형 작성
pascal = [[1]*(r+w+1) for i in range(r+w+1)]
for i in range(2, r+w):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

result = 0
k = 1
# # 조건에 맞는 합 계산
for i in range(r-1, r+w-1):
    result += sum(pascal[i][c-1:c-1+k])
    k += 1

print(result)
