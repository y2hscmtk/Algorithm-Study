# https://www.acmicpc.net/problem/15664
'''
N개의 자연수 중에서 M개를 고른 수열
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

다음수 선택시 현재수부터 고민
'''
n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split()))) # 사전순 출력을 위해 미리 정렬
visited = [False]*n # 방문 정보 확인
select = [0]*m # 선택할 수

result = set()
def make_array(start,idx):
    if idx == m:
        result.add(tuple(select))
        return
    
    # 0번째 인덱스부터 순차적으로 확인
    for i in range(start,n):
        if not visited[i]:
            visited[i] = True
            select[idx] = numbers[i]
            make_array(i+1, idx+1) 
            select[idx] = 0 # 사용 취소 처리 - 백트래킹
            visited[i] = False

make_array(0,0)

# 정답 출력
result = sorted(list(result))
for select in result:
    print(*select)