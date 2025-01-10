# https://www.acmicpc.net/problem/15654
'''
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. 
N개의 자연수는 모두 다른 수이다.
N개의 자연수 중에서 M개를 고른 수열

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''
n,m = map(int,input().split())
numbers = sorted(list(map(int,input().split()))) # 사전선 출력을 위해 미리 정렬
visited = [False]*n # 해당 인덱스의 숫자를 사용했는지 안했는지 여부를 기록
select = [0]*m # 선택할 수
def make_array(idx):
    if idx == m:
        print(*select)
        return
    
    # 0번째 인덱스부터 순차적으로 확인 - 해당 인덱스의 숫자를 이미 사용했다면 사용 불가
    for i in range(n):
        if not visited[i]: # 해당 인덱스의 숫자를 사용하지 않았다면 사용 가능
            visited[i] = True # 사용 처리
            select[idx] = numbers[i]
            make_array(idx+1)
            select[idx] = 0 # 사용 취소 처리 - 백트래킹
            visited[i] = False # 사용 취소 처리 - 백트래킹

make_array(0)
