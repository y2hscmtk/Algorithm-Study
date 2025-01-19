# 풀이 참조
'''
n개의 수가 주어졌을 때 이를 정확히 2개의 그룹 A, B로 나누어 A에 들어있는 수들의 합과 
B에 들어있는 수들의 합 간의 차이가 최소가 되도록 하는 프로그램을 작성해보세요. 
단, 주어진 n개의 수는 각각 A 또는 B 중 정확히 한 곳에만 속해야 하며, 
각 그룹은 최소 1개 이상의 수를 포함하고 있어야 함에 유의합니다.

1부터 sum(arr) 까지의 수들 중, 만들 수 있는지 없는지 여부를 2차원 배열로 정의

'''
n = int(input())
arr = [0] + list(map(int, input().split()))

m = sum(arr)
# dp[i][j] : i번째 수까지 고려했을 때, j를 만들 수 있는지 여부
dp = [[False]*(m+1) for _ in range(n+1)]
dp[0][0] = True

# i번째 수를 고려하는 상황
for i in range(1,n+1):
    for j in range(m+1):
    # 1. i번째 수를 선택하여 합이 j가 되는 경우
    # i-1번째 수까지 고려한 상황에서 i번째 수를 더했을 때 합이 j가 되어야 함
    # i-1번째 까지 고른 수들의 합이 j-arr[i]여야 한다. -> j >= arr[i] 여야 함
        if j>=arr[i] and dp[i-1][j-arr[i]]: # i-1번째 까지 고려했을때, j-arr[i]를 만들 수 있어야 함
            dp[i][j] = True # i번째 수까지 고려하여 j를 만들 수 있다.

    # 2. i번 수를 선택하지 않고, 합이 j가 된 경우
    # i번 수를 제외하고 합이 j가 되어야 함
    # i-1번째까지 고려하여 고른 수들의 합이 j여야 한다.
        if dp[i-1][j] == True:
            dp[i][j] = True # 현재 수를 선택하지 않는다.

# 그룹 A에 정확히 합 i를 만들 수 있다면
# i / m-i 로 두 그룹을 만들 수 있다.
# abs(i - (m-i)) 가 최소가 되는 경우를 갱신
ans = float('inf')
for i in range(1,m+1): # 1부터 sum(arr)까지의 수에 대해서
    if dp[n][i]: # i를 만들 수 있다면
        ans = min(ans, abs(i-(m-i)))

print(ans)

