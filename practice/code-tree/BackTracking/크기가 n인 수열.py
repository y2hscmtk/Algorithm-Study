'''
1부터 n까지의 수를 한번씩만 사용하여 만들 수 있는 모든 수열 작성
사전순 출력
'''
n = int(input())

visited = [False]*(n+1) # 각 숫자를 사용하였는지 여부 추적

selected = [0]*n
def make_array(idx):
    if idx == n:
        print(*selected)
        return    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            selected[idx] = i
            make_array(idx+1)
            selected[idx] = 0
            visited[i] = False

make_array(0)