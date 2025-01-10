# https://www.acmicpc.net/problem/15663
'''
N개의 자연수 중에서 M개를 고른 수열

중복 결과 없애기 위해 set 사용하여 저장 후 한번에 출력
'''
n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split()))) # 사전순 출력을 위해 미리 정렬
result = set()

visited = [False]*n # 방문 정보 확인
select = [0]*m # 선택할 수
def make_array(idx):
    if idx == m:
        result.add(tuple(select))
        return
    
    # 0번째 인덱스부터 순차적으로 확인
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            select[idx] = numbers[i]
            make_array(idx+1) 
            select[idx] = 0 # 사용 취소 처리 - 백트래킹
            visited[i] = False

make_array(0)

# 정답 출력
result = sorted(list(result))
for select in result:
    print(*select)