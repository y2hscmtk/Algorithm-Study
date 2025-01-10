# https://www.acmicpc.net/problem/15657
'''
N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

다음수 선택시 현재수부터 선택 시작
'''
n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split()))) # 사전선 출력을 위해 미리 정렬
select = [0]*m # 선택할 수
def make_array(start,idx):
    if idx == m:
        print(*select)
        return
    
    # 0번째 인덱스부터 순차적으로 확인
    for i in range(start,n):
        select[idx] = numbers[i]
        make_array(i,idx+1) 
        select[idx] = 0 # 사용 취소 처리 - 백트래킹

make_array(0,0)