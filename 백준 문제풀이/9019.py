# https://www.acmicpc.net/problem/9019
'''
**
n의 자릿수로 0 이 포함된 경우에 주의해야 한다. 예를 들어서 1000 에 L 을 적용하면 0001 이 되므로 결과는 1 이 된다. 
그러나 R 을 적용하면 0100 이 되므로 결과는 100 이 된다.
=> L, R 연산의 경우 숫자를 먼저 문자열로 변환시킨후 수행한다.

A,B가 주어질 때, 서로 다른 두 정수 A,B에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성
9/22 22:46 시작 23:05 종료
'''
from collections import deque
import sys

# bfs 시도 23:17
def bfs():
    queue = deque()
    # A 와 B는 모두 0 이상 10,000 미만이다.
    visited = [False for _ in range(10001)]
    visited[A] = True
    queue.append((A,'')) # 현재 문자열과 도달하기 위한 명령어
    while queue:
        n,p = queue.popleft()
        if n == B:
            return p
        # D 연산
        next_n = (2 * n) % 10000
        if not visited[next_n]:
            visited[next_n] = True
            queue.append((next_n, p + 'D'))
        # S 연산
        next_n = 9999 if n == 0 else n - 1
        if not visited[next_n]:
            visited[next_n] = True
            queue.append((next_n, p + 'S'))
        # L 연산
        next_n = (n % 1000) * 10 + n // 1000
        if not visited[next_n]:
            visited[next_n] = True
            queue.append((next_n, p + 'L'))
        # R 연산
        next_n = (n % 10) * 1000 + n // 10
        if not visited[next_n]:
            visited[next_n] = True
            queue.append((next_n, p + 'R'))

# A를 B로 바꾸는 최소 명령어 생성
def dfs(n,depth):
    global result,min_count
    # B를 넘어서게 될 경우 볼 필요없음
    if depth > min_count: # 설정된 최소횟수보다 더 많은 연산이 수행될 경우, 해당 수행에 대해서는 검토할 필요없음
        return
    # B에 도달하는데 성공하였고, 기존 최소횟수보다 더 단축되었다면
    if n == B and depth < min_count:
        min_count = depth # 최소횟수 갱신하고 현재 수행 종료
        return
    # DSLR 차례로 수행
    
    # D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 
    # 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
    next_n = n*2%10000
    result.append("D")
    dfs(next_n, depth+1)
    result.pop()
    
    # S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. 
    next_n = 9999 if n == 0 else n-1 # n이 0 이라면 9999 가 대신 레지스터에 저장된다.
    result.append("S")
    dfs(next_n,depth+1)
    result.pop()
    
    # L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 
    # 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
    # 1234 →L 2341 →L 3412
    str_n = str(n)
    next_n = ''
    for i in range(1,len(str_n)):
        next_n += str_n[i]
    next_n += str_n[0]
    next_n = int(next_n) # 다시 정수로 변환
    result.append("L")
    dfs(next_n,depth+1)
    result.pop()
    
    # R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 
    # 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
    # 1234 →R 4123 →R 3412
    str_n = str(n)
    next_n = str_n[-1]
    for i in range(len(str_n)-1):
        next_n += str_n[i]
    next_n = int(next_n) # 다시 정수로 변환
    result.append("R")
    dfs(next_n,depth+1)
    result.pop()
    
for _ in range(int(input())): # T개의 테스트 케이스가 주어진다.
    A, B = map(int,input().split())
    # result = [] # 최소 명령 횟수 저장용
    # min_count = sys.maxsize # 최소 변환 횟수
    # dfs(A,0) # 초기 숫자 주입 A
    # print(result)
    print(bfs())