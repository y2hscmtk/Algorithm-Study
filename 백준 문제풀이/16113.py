# https://acmicpc.net/problem/16113
'''
<아이디어>
0. 각 숫자들의 형태를 담은 2차원 배열을 미리 만들어 둔다.
1. 주어진 문자열을 5줄의 문자열로 만든다.(5의 배수)
2. 각 자리의 숫자가 1인지 아닌지 검사한다.
    2.1. '#'이 일자로 쭉 늘어지면서, 양옆이 모두 '.'이라면 1이다.
3. 1이 아니라면 미리 만들어둔 문자열과 비교하여 어떤 수인지 파악하여 출력한다.
'''
zero = [["#","#","#"],
        ["#",".","#"],
        ["#",".","#"],
        ["#",".","#"],
        ["#","#","#"]]

one = []

two = [["#","#","#"],
        [".",".","#"],
        ["#","#","#"],
        ["#",".","."],
        ["#","#","#"]]

three = [["#","#","#"],
        [".",".","#"],
        ["#","#","#"],
        [".",".","#"],
        ["#","#","#"]]

four = [["#",".","#"],
        ["#",".","#"],
        ["#","#","#"],
        [".",".","#"],
        [".",".","#"]]

five = [["#","#","#"],
        ["#",".","."],
        ["#","#","#"],
        [".",".","#"],
        ["#","#","#"]]

six = [["#","#","#"],
        ["#",".","."],
        ["#","#","#"],
        ["#",".","#"],
        ["#","#","#"]]

seven = [["#","#","#"],
        [".",".","#"],
        [".",".","#"],
        [".",".","#"],
        [".",".","#"]]

eigth = [["#","#","#"],
        ["#",".","#"],
        ["#","#","#"],
        ["#",".","#"],
        ["#","#","#"]]

nine = [["#","#","#"],
        ["#",".","#"],
        ["#","#","#"],
        [".",".","#"],
        ["#","#","#"]]

# 0. 미리 숫자들 만들어 두기, 1은 따로 검사할것이므로 만들 필요 없다.
numbers = [zero,one,two,three,four,five,six,seven,eigth,nine]
n = int(input())
data = list(input())
# 해석한 문자(5줄로 분리)
length = n//5 # 한 줄에 포함될 문자열의 개수
signal = [data[i:i+length]for i in range(0,n,length)]
visited = [False for _ in range(length)] # 맨 윗줄만 검사할것이므로 한줄만 있어도됨

def isOne(i):
    # 세로로 모두 "#"이고, 양옆의 좌표가 .또는 갈수없는 곳이라면 1임
    for j in range(5):
        if signal[j][i] == "#":
            # 좌,우 확인
            if i-1>=0:
                if signal[j][i-1] != ".":
                    return False
            if i+1<length:
                if signal[j][i+1] != ".":
                    return False
    print(1,end='')
    # 방문처리
    visited[i] = True
    return True

def decryption(start):
    # 주어진 시작 좌표의 3*5크기의 배열과 미리 만들어둔 배열을 비교
    number_area = [signal[i][start:start+3] for i in range(5)]
    for i,num in enumerate(numbers):
        if num == number_area:
            print(i,end='')
            
    # 가로 3칸 방문처리
    visited[start:start+3] = [True,True,True]
    return

for i in range(length):
    # 아직 탐색하지 않은 숫자에 대해서만
    if not visited[i] and signal[0][i] == '#':
        # 1인지 검사
        if isOne(i):
            continue
        decryption(i) # 복호화하여 출력
