# 부분 수열의 합이 k
'''
N개의 정수로 이루어진 수열에서 연속된 구간의 합을 구하라
연속된 구간의 합 중에서 합이 K인 것의 개수를 구하라
'''
N,K = map(int,input().split())
arr = list(map(int,input().split()))

# 누적합 배열 생성
pf = [0] * (N+1)
for i in range(1,N+1):
    pf[i] = pf[i-1] + arr[i-1]

result = 0
# 길이를 몇으로 둘 것인지 설정
for length in range(1,N+1): # 최대 N까지 가능
    for i in range(length, N+1):
        if pf[i] - pf[i-length] == K:
            result += 1

print(result) 
