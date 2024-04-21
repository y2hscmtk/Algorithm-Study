# https://www.acmicpc.net/problem/1038
'''
N번째 감소하는 수를 출력하라.
N번째 감소하는 수가 없다면 -1을 출력한다.
감소하는 수는 유한 할 수 밖에 없다.(9876543210이 한계임)
'''
import sys
input = sys.stdin.readline
N = int(input())
number = []
result = set()

def dfs(last):
    for i in range(last,-1,-1):
        number.append(i)
        result.add(int(''.join(map(str,number))))
        dfs(i-1)
        number.pop()
# 앞자리는 0~9로 시작 가능
for i in range(10): 
    dfs(i)
# 감소하는 수는 최대 1023개임(0~9876543210)
print(sorted(list(result))[N]) if N<1023 else print(-1)