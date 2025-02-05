n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
pf = [[0]*(n+1) for _ in  range(n+1)]

# 2차원 누적합 배열 생성
for i in range(n):
    for j in range(n):
        pf[i+1][j+1] = pf[i][j+1] + pf[i+1][j] - pf[i][j] + arr[i][j]

# k * k 크기의 정사각형 설정시 최대값
result = 0
for i in range(k,n+1):
    for j in range(k,n+1):
        # (i-k,j-k) ~ (i,j) 설정
        result = max(result, pf[i][j] - pf[i-k][j] - pf[i][j-k] + pf[i-k][j-k])

print(result)