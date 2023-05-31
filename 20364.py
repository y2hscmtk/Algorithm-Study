# https://www.acmicpc.net/problem/20364

'''
목적지에서부터 1에 이르기까지
부모에서 부모로 거슬러 올라간다.
끝까지 거슬러 올라가서 1에 도달하였다면 
=> 목적지에 도달할때까지 점유된 땅이 없었다는 의미
1에 도달하기 이전에 점유한 땅이 발견되었다면
=> 목적지에 도달하지 못한다는 의미이므로, 가장 작은 수의 점유된 땅으로 업데이트
(가장 처음 만나는 점유된 땅이어야 하므로)
'''
import sys
input = sys.stdin.readline
n,q = map(int,input().split())

# 점유한 땅을 기록하기 위한 배열
visited = set()

for _ in range(q):
    target = int(input()) # 도달하고자 하는 목적지
    node = target
    success = True # 목적지에 도달하는데 성고하였는지 여부를 저장하기 위함
    result = target #
    while node!=1: # 1에 도달할때까지 반복
        # 점유한 땅에 도달하였는지 확인
        if node in visited:
            success = False # 도달하는데 실패
            result = node
        node//=2 # 부모 노드로 이동
        
    if not success: # 성공하지 못했다면 result 출력
        print(result)
    else:
        print(0) # 성공하였다면 0출력
        visited.add(target) # 점유한 땅에 삽입
