'''
내림차순으로 정렬될때 가장 큰 상금을 획득할 수 있다.
반드시 정해진 숫자만큼 교환을 해야한다.
같은 자리를 여러번 선택하여 교환해도 괜찮다.
'''
# curr : 현재 숫자
# depth : 교환 횟수 - 깊이
def dfs(curr, depth):
    global result
    # 동일한 상태(현재 상태, 교환 횟수)가 반복되지 않도록
    state = (tuple(curr), depth)
    if state in visited:
        return
    visited.add(state)
    
    if depth == t:
        # 교환 횟수를 다 사용한 경우 결과 갱신
        result = max(result, int(''.join(curr)))
        return
    
    for i in range(len(curr)):
        for j in range(i+1,len(curr)):
            curr[i],curr[j] = curr[j],curr[i] # 스왑
            dfs(curr, depth+1)
            curr[j],curr[i] = curr[i],curr[j] # 스왑 취소 - 백트래킹

for i in range(1,int(input())+1):
    p, t = input().split() # 숫자판 정보, 교환횟수
    t = int(t)
    result = 0
    visited = set() # 중복방문 방지
    dfs(list(p),0)
    print(f'#{i} {result}')