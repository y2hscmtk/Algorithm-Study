# 1이상 k 이하의 숫자를 하나 고르는 행위를 N번 반복하여 나올 수 있는
# 서로 다른 순서쌍 출력, 단, 연속해서 같은 수가 3번 이상 나오는 경우는 불가능

K,N = map(int,input().split())

select = [0]*N # N개 고르기    

def dfs(cnt):
    if cnt == N:
        print(*select)
        return
    
    for i in range(1,K+1):
        # 숫자가 이미 2 이상 쌓여있는 상황에 대해
        # 이전 숫자와 그 이전의 숫자가 현재 숫자와 모두 같은 경우는 불가능
        if cnt>=2 and (select[cnt-1] == select[cnt-2] and select[cnt-1] == i):
            continue
        select[cnt] = i
        dfs(cnt+1)
        select[cnt] = 0 # 백트래킹

dfs(0)
    