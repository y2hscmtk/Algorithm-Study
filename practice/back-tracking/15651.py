# https://www.acmicpc.net/problem/15651
'''
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''
n,m = map(int,input().split())
select = [0]*m # 선택할 숫자들

def make_array(idx):
    if idx == m:
        print(*select)
        return
    
    # 1부터 n까지 자연수 중에 중복으로 선택 가능
    for num in range(1,n+1):
        select[idx] = num
        make_array(idx+1)
        select[idx] = 0 # 백트래킹

make_array(0)