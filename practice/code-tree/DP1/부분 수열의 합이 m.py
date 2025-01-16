'''
수열 원소의 위치 변경 불가능 -> 정렬해도 상관은 없을듯?
수열 내 원소의 합이 m이 되는 경우 중 가능한 최소 수열의 길이
-> 값을 하나씩만 사용 가능
'''
n, m = map(int, input().split())
A = sorted(list(map(int, input().split())))

INF = float('inf')
dp = [INF]*(m+1)
dp[0] = 0

# 사용할 수 선택
for num in A:
    # 거꾸로 값을 채워넣어 한번만 수를 사용하여 조합을 만들도록 설계
    for i in range(m,-1,-1):
        if i-num>=0: # 인덱스 범위 체크
            dp[i] = min(dp[i],dp[i-num] + 1)


if dp[m] == INF:
    print(-1)
else:
    print(dp[m])
