# https://www.acmicpc.net/problem/3003

# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

collect = [1, 1, 2, 2, 2, 8]
data = list(map(int, input().split()))

for i in range(6):
    print(collect[i]-data[i], end=' ')
