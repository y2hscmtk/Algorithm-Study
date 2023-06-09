# https://www.acmicpc.net/problem/2164
'''
12345678 (짝수의 경우)
=> 2468만 남게됨
123456789 (홀수의 경우)
=> 2468남은 후, 4682로 변환됨
'''
from collections import deque
import sys
n = int(input())

if n<2:
    print(1)
    sys.exit(0)
else:
    data = deque([i for i in range(2,n+1,+2)])
    
# n이 만약에 홀수였다면 배열 변형필요
if n%2!=0:
    data.append(data.popleft()) # 앞에 수를 뽑아서 뒤에 배치

# 큐의 길이가 3이 될때까지 제거 작업 반복
while True:
    if len(data)==1:
        print(*data)
        break
    data.popleft() # 가장 왼쪽 수를제거
    data.append(data.popleft())
        
