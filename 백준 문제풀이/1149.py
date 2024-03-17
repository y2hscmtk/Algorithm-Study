# https://www.acmicpc.net/problem/1149
'''
인접한 칸 끼리는 서로 다른 색이어야 함
자신의 색을 제외한 다른 색을 선택 할 수 있으므로 항상 2가지 경우의 수가 존재
세로 : 집 번호
가로 : R G B 비용
arr[0][1] => 0번째 집을 1번 색으로 칠할 때의 비용
     R  G  B
0    26 40 83
1    49 60 57
2    13 89 99
R B R => 26 + 57 + 13 = 96 정답
dp[i][j] => i번째 칸을 색상 j로 칠할 때의 최소 비용
dp[i][j] = min(dp[i-1][j-1],dp[i-1][j+1] => j가 아닌 수(다른 색상)) + arr[i][j]
res = min(dp[n])
편의를 위해 왼쪽 맨 끝과 최상단을 0으로 패딩
'''
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*4 for _ in range(n+1)] # 편의를 위해 패딩
# N까지 이를때까지
for i in range(1,n+1):
    # 값 삽입시, 이전에 선택한 비용은 현재 색상이 아닌 색상만 비교
    for j in range(1,4):
        check = []
        for k in range(1,4):
            if k == j:
                continue
            check.append(dp[i-1][k])
        dp[i][j] = min(check) + arr[i-1][j-1]

print(min(dp[n][1:]))