# https://www.acmicpc.net/problem/3098
'''
사람들은 매일 조상님들의 말씀을 따르기 위해서 자신의 친구의 친구 목록을 확인하고, 이를 모두 자신의 친구로 추가한다.
=> 각 사람들에 대해서 반복한다.
모든 친구관계는 대칭이다. 즉, A와 B의 친구라면, B도 A의 친구이다.
=> 양방향 그래프이다.

사람의 수와 지금 친구 관계가 주어졌을 때, 모든 사람이 서로 친구가 되는데 걸리는데 며칠이 걸리는지 구하는 프로그램을 작성하시오. 
또한, 매일 매일 새로운 친구 관계가 얼마나 생기는지 구해서 출력하시오.

=> 구현, 시뮬레이션, 그래프 이론
'''
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
# 최초의 관계
graph = [[] for _ in range(N+1)]
friendCount = []
for _ in range(M):
    A,B = map(int,input().split())
    # 모든 친구관계는 대칭이다.
    graph[A].append(B)
    graph[B].append(A)

# 친구관계 시뮬레이션
K = 0 # 모든 사람들이 친구가 되는데 걸리는 시간
while True:
    # 1. 모든 사람들이 친구가 되었다면 종료
    allFriend = True
    for i in range(1,N+1):
        if len(graph[i]) != N-1: # 본인제외
            allFriend = False
            break
    if allFriend: # 모든 사람이 친구라면
        break
    # 2. 각 사람에 대해서 친구관계 확장 수행
    newFriend = [[j for j in graph[i]] for i in range(N+1)]
    count = 0 # 오늘 생긴 친구관계 카운팅
    for i in range(1,N+1):
        if len(newFriend[i]) == N-1: # 모두 친구가 완성되었다면 다른 사람으로 진행
            continue
        
        # 3. 자신의 친구들의 친구들을 확인한다.
        for friend in graph[i]: 
            for p in graph[friend]:
                if p<=i: # ** 자신보다 이전 번호의 친구는 이전 반복문에서 검사하였으므로 넘어간다.
                    continue
                if p not in newFriend[i]: # 자신과 친구관계에 있지 않다면
                    newFriend[i].append(p)
                    newFriend[p].append(i)
                    count+=1 # 친구관계 카운팅 + 1
    
    # 4. 친구를 받아주는데는 하루가 걸린다.
    K+=1
    # 친구관계 업데이트
    graph = [[j for j in newFriend[i]] for i in range(N+1)]
    friendCount.append(count) # 오늘 생긴 친구관계 수 저장


# 모든 사람들이 친구가 되는데 걸리는 시간(K)을 구하고
print(K)
# 다음 K의 줄에는 몇 명의 새로운 관계가 생기는지, 첫날부터 K번째 날 까지 하나씩 출력
for f in friendCount:
    print(f)
