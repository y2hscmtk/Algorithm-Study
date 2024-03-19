# https://www.acmicpc.net/problem/15664
'''
오름차순으로 출력해야 하므로 우선 정렬
visited 배열 사용해서 중복으로 선택하지 않도록
'''
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = list(map(int,input().split()))

def dfs(curr,start):
    if len(curr) == m: # 원하는 길이만큼 수를 찾았다면
        print(*curr)
        return
    # 2 4 4 와 같은 경우에서 같은 수를, 같은 자리에 연속해서 채택하지 않도록 하는것이 목표
    used = [False]*max(data)
    for i in range(start,n):
        num = data[i]
        if not used[num]: # 해당 수를 이번 자리에서 사용한적이 없다면
            used[num] = True # 사용처리
            curr.append(num) # 자리에 수 올리기
            dfs(curr,i+1)
            # 백트래킹
            curr.pop() # 다음 수로 이동하기 위해, used[num]은 다음에 같은 수가 올수있으므로 변경x

data.sort() # 편의를 위해 오름차순 정렬
dfs([],0)