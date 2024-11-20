# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
'''
완전탐색, 브루트포스
1. 탐색을 시작할 한 점 선택
2. 대각선 그리며 각 카페 방문 - 범위 검사, 중복 검사, 최소값 업데이트
디저트를 가장 많이 먹을 수 있는 경로를 찾고, 그 때의 디저트 수를 정답으로 출력하는 프로그램을 작성하라.
만약, 디저트를 먹을 수 없는 경우 -1을 출력한다.
카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안 된다.
디저트 종류를 나타나는 수는 1 이상 100 이하의 정수이다.
'''
for tc in range(1,1+int(input())):
    result = -1 # 섭취할 수 있는 디저트 개수
    N = int(input()) # 배열 사이즈 N x N
    graph = [list(map(int,input().split())) for _ in range(N)]
    
    # 1. 탐색 시작할 점(i,j) 선택
    for i in range(N):
        for j in range(1,N-1): # 각 끝점은 시작 지점으로 선택 불가 -> 마름모 형성 불가능            
            # 각 대각선을 얼마나 늘릴것인지 선택 최대 N(가장 긴 대각선)
            for di in range(1,N+1):
                for dj in range(1,N+1):
                    isFail = False
                    visited = set()
                    ni,nj = i,j
                    visited.add(graph[ni][nj])
                    for si in range(i,i+di+dj):
                        if si<i+di:
                            ni+=1;nj-=1
                        else:
                            ni+=1;nj+=1
                        if 0<=ni<N and 0<=nj<N and graph[ni][nj] not in visited:
                            visited.add(graph[ni][nj])
                        else:
                            isFail = True
                            break
                    if isFail:
                        continue
                    ni,nj = i,j
                    for si in range(i,i+di+dj-1):
                        if si<i+dj:
                            ni+=1;nj+=1
                        else:
                            ni+=1;nj-=1
                        if 0<=ni<N and 0<=nj<N and graph[ni][nj] not in visited:
                            visited.add(graph[ni][nj])
                        else:
                            isFail = True
                            break
                    if isFail == False:
                        result = max(result,len(visited))
                    
    print(f'#{tc} {result}')