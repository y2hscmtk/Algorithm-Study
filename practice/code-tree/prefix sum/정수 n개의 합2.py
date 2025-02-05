INT_MAX = float('inf')
n,k = map(int,input().split())
arr = list(map(int,input().split()))

pf = [0]*(n+1)
for i in range(1,n+1):
    pf[i] = pf[i-1] + arr[i-1]

# 구간별 합 계산
result = -INT_MAX
# 길이를 k로 두었을 때, 연속합 중 최대값 갱신
for i in range(k,n+1):
    result = max(result, pf[i]-pf[i-k])

print(result)