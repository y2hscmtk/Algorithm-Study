# https://www.acmicpc.net/problem/3273
'''
N의 범위 100000이므로 투포인터가 적당해보임
'''
import sys
input = sys.stdin.readline
n = int(input())
numbers = sorted(list(map(int,input().split())))
x = int(input())

result = 0 # 몇개의 쌍이 가능한지
# ai 고정시켜두고, ai 이후의 수들에 대해서 aj를 달리하며 x가 될 수 있는지 판별
for i in range(n):
    start = numbers[i]
    if start>x: # 두 수를 더해야 하는데 한 수만으로도 더 커진다면 어차피 불가능
        break
    for j in range(i+1,n): # i 이후의 수에 대해서
        end = numbers[j]
        SUM = start + end
        if SUM > x: # 정렬되어 있으므로 더했을 때 x보다 크다면 이후의 수도 불가능
            break
        elif SUM == x: # 목표 달성시
            result+=1
print(result)
