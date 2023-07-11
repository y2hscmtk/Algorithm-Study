# https://www.acmicpc.net/problem/9655
n = int(input())

dp = [False for _ in range(n+1)]
dp[1] = "SK"  # 시작은 상근이
for i in range(1, n+1):
    # 기록이 안돼있다면
    # 이전 사람과 다른 사람으로 기록후, 한칸, 세칸 후 사람으로 이전사람 지정
    if not dp[i]:
        last = dp[i-1]
        dp[i] = "CY" if last == "SK" else "SK"
        if i+1 <= n:
            dp[i+1] = last
        if i+3 <= n:
            dp[i+3] = last
