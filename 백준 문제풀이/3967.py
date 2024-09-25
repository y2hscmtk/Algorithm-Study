# https://www.acmicpc.net/problem/3967
'''
매직 스타
구현, 백트래킹, 브루트포스
1. 각 방향을 더하는 함수 작성
2. 비워져 있는 칸을 저장하기 위한 배열 생성
3. 비워져 있는 칸에 문자를 저장하면서 다 채워졌을 때 각 방향 더하기 수행

** 수가 채워져 있지 않은 곳은 x로, 채워져 있는 곳은 'A'부터 'L'까지 알파벳으로 채워져 있다
**  i번째 알파벳은 숫자 i를 의미한다. '.'는 매직 스타의 형태를 만들기 위해서 사용하는 문자이다. 
'''
import sys
# 1. 빈칸 위치 확인 필요
blank = []

# 2. 사용한 문자, 사용하지 않은 문자 확인 필요
alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12}
alphabet_num = ['','A','B','C','D','E','F','G','H','I','J','K','L']
isUsed = [False for i in range(13)] # 해당 문자를 사용하였는지 사용하지 않았는지 확인하는 용도

positions_list = [(0,4),(1,1),(1,3),(1,5),(1,7),(2,2),(2,6),(3,1),(3,3),(3,5),(3,7),(4,4)]
lines = [
    [0,2,5,7],   # line0
    [0,3,6,10],  # line1
    [7,8,9,10],  # line2
    [1,5,8,11],  # line3
    [4,6,9,11],  # line4
    [1,2,3,4]    # line5
]


# 원본 데이터 저장용
data = []
for i in range(5):
    row = list(input())
    for j in range(len(row)):
        if row[j] == 'x': # 빈칸 발견시
            blank.append((i,j)) # 빈칸 위치 
        elif row[j] != '.':

            isUsed[alphabet[row[j]]] = True # 문자 사용 처리
    data.append(row)

        
# 모든 방향의 수를 더해서 모두 26이 만족되면 true
def check():
    # 왼쪽 대각선
    sum = 0
    for x,y in [(0,4),(1,3),(2,2),(3,1)]:
        sum+=alphabet[data[x][y]]
    if sum != 26:
        return False
    # 오른쪽 대각선
    sum = 0
    for x,y in [(0,4),(1,5),(2,6),(3,7)]:
        sum+=alphabet[data[x][y]]
    if sum != 26:
        return False
    # 아래 선
    sum = 0
    for x,y in [(3,1),(3,3),(3,5),(3,7)]:
        sum+=alphabet[data[x][y]]
    if sum != 26:
        return False
    # 왼쪽 역 대각선
    sum = 0
    for x,y in [(1,1),(2,2),(3,3),(4,4)]:
        sum+=alphabet[data[x][y]]
    if sum != 26:
        return False
    # 오른쪽 역 대각선
    sum = 0
    for x,y in [(1,7),(2,6),(3,5),(4,4)]:
        sum+=alphabet[data[x][y]]
    if sum != 26:
        return False
    # 위 선
    sum = 0
    for x,y in [(1,1),(1,3),(1,5),(1,7)]:
        sum+=alphabet[data[x][y]]
    if sum != 26:
        return False

    return True # 모든 줄의 합이 26인 경우

    

def dfs(curr,depth):
    global data
    # 모든 빈칸을 다 채웠는지 확인
    if depth == len(blank):
        # 조건을 만족하는지 확인 => 각 방향의 수를 더했을 때 26이 되는지 확인
        if check():
            # 현재 완성된 화면을 출력한 뒤 시스템 종료
            for row in data:
                for i in range(len(row)):
                    print(row[i],end='')
                print()
            sys.exit()
        return # 조건을 만족하지 않는다면 다음 경우의 수 탐색
    
    # 각 빈칸에 대해서 아직 사용하지 않은 알파벳을 하나씩 채워나간다.
    for i in range(curr,len(blank)):
        x,y = blank[i]
        for a in range(1,len(isUsed)):
            if isUsed[a] == False: # 아직 해당 문자를 사용하지 않았다면
                isUsed[a] = True
                data[x][y] = alphabet_num[a]
                dfs(i+1,depth+1)
                # 백트래킹
                data[x][y] = 'x'
                isUsed[a] = False
dfs(0,0)