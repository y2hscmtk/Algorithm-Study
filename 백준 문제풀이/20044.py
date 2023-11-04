# https://www.acmicpc.net/problem/20044
import sys
n = int(input())
data = sorted(list(map(int, input().split())))
result = sys.maxsize
# 양 끝에서 2개씩 짝을 지으면 될듯?
for i in range(n):
    result = min(result, data[i]+data[2*n-1-i])
    # 0,1,2,3 ; n = 2 => 2*n = 4
    # i = 0; 2*n-1-i => 4-1-0 = 3
    # i = 1; 2*n-1-i => 4-1-1 = 2
print(result)
