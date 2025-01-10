# https://www.acmicpc.net/problem/15650
'''
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

오름차순이고, 중복이 없으므로 -> 현재 수보다 이후의 수를 다음에 고르면 문제없음
'''
n,m = map(int,input().split())
is_used = [False]*(n+1) # 각 숫자를 사용했는지 안했는지 여부 확인용
select = [0]*m # 선택할 숫자들
def make_array(start,idx):
    if idx == m:
        print(*select)
        return
    for num in range(start+1,n+1):
        select[idx] = num
        make_array(num, idx+1) # num 이후의 수에 대해서 선택
        select[idx] = 0

make_array(0,0)