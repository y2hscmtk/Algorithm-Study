# https://www.acmicpc.net/problem/10810
N,M = map(int,input().split())
bocket = [0]*N
# i부터 j까지 k로 교체
for _ in range(M):
    i,j,k = map(int,input().split())
    for l in range(i-1,j):
        bocket[l] = k
print(*bocket) # 정답 출력