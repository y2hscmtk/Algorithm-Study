# https://www.acmicpc.net/problem/15649
'''
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
(1 ≤ M ≤ N ≤ 8)
'''
n, m = map(int,input().split())
select = [0]*m # m개 선택하기
def make_array(idx):
    # 재귀함수 종료조건
    if idx == m: # m번째 인덱스까지 도달시 종료(출력)
        print(*select)
        return
    # 1 부터 n까지의 수 중에 선택
    for num in range(1,n+1):
        if num not in select:
            select[idx] = num
            make_array(idx+1)
            select[idx] = 0 # 선택 취소

make_array(0)

# m개를 선택하는 과정에 대해서 n개의 수에 대해 모두 선택가능 여부 검사
# 시간 복잡도 : O(m^n)