# https://www.acmicpc.net/problem/1342
'''
인접해 있는 모든 글자가 같지 않은 문자를 행운의 문자열이라고 한다.
문자열 S에 나오는 모든 문자를 재배치 하면, 서로 다른 행운의 문자열이 몇개 나오는가
S의 길이는 최대 10, 알파벳 소문자로만 이루어져있다.
'''
def dfs(curr,used):
    # 모든 문자를 다 사용하였다면 행운의 문자열인지 검사
    if len(curr) == len(S):    
        for i in range(1,len(curr)):
            if curr[i] == curr[i-1]: # 인접한 문자가 서로 다른 문자인지 확인
                return
        # 인접한 문자가 서로 다른 문자라면 => 행운의 문자열
        lucky.add(str(curr))
        return
    # 글자를 모두 사용할 때 까지 재귀 호출
    # S문자열의 각 인덱스는 한번만 사용되어야 함
    for i in range(len(S)):
        if not used[i]: # i번째 글자를 아직 사용하지 않았다면
            used[i] = True # 사용 처리
            curr.append(S[i])
            dfs(curr,used)
            # 백트래킹
            curr.pop() 
            used[i] = False

S = input()
lucky = set() # 행운의 문자열을 저장하기 위해
used = [False]*len(S)
dfs([],used)
print(len(lucky))

