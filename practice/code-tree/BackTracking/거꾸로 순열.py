'''
1부터 n까지의 수 한번씩 사용, 내림차순으로 출력
'''
n = int(input())

visited = [0]*(n+1)
selected = [0]*n

def make_array(idx):
    if idx == n:
        print(*selected)
        return
    
    for i in range(n,0,-1):
        if not visited[i]:
            visited[i] = True
            selected[idx] = i
            make_array(idx+1)
            selected[idx] = 0
            visited[i] = False

make_array(0)            