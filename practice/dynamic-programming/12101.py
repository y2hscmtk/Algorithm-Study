# https://www.acmicpc.net/problem/12101
def dfs(curr,formula):
    global cnt,result
    if cnt > k or curr > n:
        return
    if curr == n:
        if cnt == k:
            result = formula
        cnt+=1
        return
    for i in range(1,4):
        dfs(curr+i,f'{formula}+{i}')
    
n,k = map(int,input().split())
cnt = 1 # 몇번째 수인지
result = '-1'
for i in range(1,4):
    dfs(i,f'{i}')
print(result)