# https://www.acmicpc.net/problem/22233
'''
딕셔너리 활용, 아직 사용하지 않은 수 카운팅 필요
16:56 ~ 17:02
'''
import sys
input = sys.stdin.readline
memo = {}
N, M  = map(int,input().split())
curr_result = N # 사용하지 않은 키워드 수
for _ in range(N):
    keyword = input().rstrip() # 메모장에 적을 키워드
    memo[keyword] = False # 메모 기록 및 사용 한적 없음 처리
    
for _ in range(M):
    post = input().rstrip().split(",")
    # 가희가 적은 포스트에 대해서
    for p in post:
        # 메모된 키워드이며 사용한적 없는 경우 사용처리 후 잔여 사용가능횟수 -1
        if p in memo and memo[p] == False: # 사용한적 없다면
            memo[p] = True # 사용 처리
            curr_result -= 1
    print(curr_result) # 잔여 횟수 출력