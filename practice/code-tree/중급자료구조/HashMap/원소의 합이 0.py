# 원소의 합이 0
'''
네 개의 수열 A, B, C, D에서 각각 원소를 하나씩 골라 더하였을 때 합이 0이되는 경우의 수를 구하는 프로그램을 작성해보세요.

풀이 참조
'''
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))

count = dict()
# 1. A & B에서 나올 수 있는 합 기록
for i in range(n):
    for j in range(n):
        sum = A[i] + B[j]
        if sum in count:
            count[sum] += 1
        else:
            count[sum] = 1

result = 0
# 2. C & D에서 나올 수 있는 합의 역수가 HashMap에 기록되어있다면 0이 되는 경우에 해당
for i in range(n):
    for j in range(n):
        target = -(C[i] + D[j])
        if target in count:
            result += count[target]

print(result)