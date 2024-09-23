# https://www.acmicpc.net/problem/17394
'''
목표치 A 이상 B 이하인 소수로 인구를 줄이려 한다
Sonaht는 최대한 적은 수의 핑거 스냅으로 이 목표를 달성하고자 한다. Sonaht가 최소 몇 번의 핑거 스냅을 해야 할지 구해보자.
** 만약 목표범위 내의 소수로 만들 수 없다면, -1을 출력한다.
** 2 ≤ A ≤ B ≤ 100,000
09/24 01:10 시작 01:25 제출 -> 인덱스 에러; 01:27 수정 후 제출 -> 정답
'''
from collections import deque
from math import sqrt

# 최단거리 -> bfs
# 4가지 수행에 대해서 목표치에 도달하였는지 확인 -> 소수인지 확인
def bfs(start):
    queue = deque()
    # 2 ≤ A ≤ B ≤ 100,000
    visited = [-1 for _ in range(1000001)]
    visited[start] = 0 # 방문처리
    queue.append(start)
    while queue:
        x = queue.popleft()
        # 목표치에 도달하였는지 확인
        if A<=x and x<=B:
            # 소수인지 확인
            if x%2 != 0: # 소수는 1과 자기자신만을 약수로 가지므로 짝수가 될수 없음
                isPrime = True
                for i in range(3,int(sqrt(x))+1,2): # 3이상의 홀수를 기준으로 나누어 떨어지는지 확인
                    if x%i == 0:
                        isPrime = False
                        break
                if isPrime: # 소수라면 최소 횟수 리턴    
                    return visited[x]

        # (아래의 두 경우에서, 나누어 떨어지지 않으면 몫만 남기고, 나머지는 버린다.)
        # 1. 전 우주의 생명체를 절반으로 줄인다.
        if 0<=(x//2)<1000001 and visited[x//2] == -1:
            visited[x//2] = visited[x] + 1
            queue.append(x//2)
        # 2. 전 우주의 생명체 수를 현재의 1/3로 한다.
        if 0<=(x//3)<1000001 and visited[x//3] == -1:
            visited[x//3] = visited[x] + 1
            queue.append(x//3)

        # (이미 전 우주의 생명체 수가 0이라면 할 수 없다.)
        if x!=0:
            if 0<=x+1<1000001 and visited[x+1] == -1:
                # 3. 전 우주의 생명체 수를 현재보다 하나 늘린다.
                visited[x+1] = visited[x] + 1
                queue.append(x+1)
            # 4. 전 우주의 생명체 수를 현재보다 하나 줄인다.
            if 0<=x-1<1000001 and visited[x-1] == -1:
                visited[x-1] = visited[x] + 1
                queue.append(x-1)
    return -1


for _ in range(int(input())):
    N,A,B = map(int,input().split())
    print(bfs(N))

