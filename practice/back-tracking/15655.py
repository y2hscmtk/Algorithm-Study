# https://www.acmicpc.net/problem/15655
'''
N개의 자연수 중에서 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

현재 수 이후의 수에 대해서 선택하면 문제없음
'''
n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split()))) # 사전선 출력을 위해 미리 정렬
select = [0]*m # 선택할 수
def make_array(start,idx):
    if idx == m:
        print(*select)
        return
    
    # 0번째 인덱스부터 순차적으로 확인 - 해당 인덱스의 숫자를 이미 사용했다면 사용 불가
    for i in range(start,n):
        select[idx] = numbers[i]
        make_array(i+1, idx+1) # 현재 수 이후의 수부터 탐색
        select[idx] = 0 # 사용 취소 처리 - 백트래킹

make_array(0,0)