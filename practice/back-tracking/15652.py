# https://www.acmicpc.net/problem/15652
'''
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

오름차순 => 다음수 선택시 현재수부터 선택하면 문제없음
'''
n,m = map(int,input().split())
select = [0]*m # 선택할 숫자들

def make_array(start,idx):
    if idx == m:
        print(*select)
        return
    
    # 1부터 n까지 자연수 중에 중복으로 선택 가능
    for num in range(start,n+1):
        select[idx] = num
        make_array(num,idx+1) # num부터 선택 시작
        select[idx] = 0 # 백트래킹

make_array(1,0) # 1부터 시작