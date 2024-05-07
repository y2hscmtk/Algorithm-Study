# https://www.acmicpc.net/problem/11652
import sys
dict = {}
for _ in range(int(input())):
    n = int(input())
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1

max_count = -1
result = sys.maxsize
for key,value in dict.items():
    if value >= max_count:
        if value == max_count:
            result = min(result,key)
        else:
            max_count = value
            result = key
print(result)
        