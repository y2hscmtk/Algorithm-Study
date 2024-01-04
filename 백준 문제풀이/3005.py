# https://www.acmicpc.net/problem/3005
'''
'#' 을 만나기전까지 돌면서, 문자 만들고 만들어진 글자가 2글자 이상이라면 words에 삽입
words 배열을 정렬한 뒤, 첫번재 문자 출력
'''
r,c = map(int,input().split())
words = []
data = [list(input()) for _ in range(r)]
# 가로로 만들 수 있는 문자 삽입
for i in range(r):
    word = ''
    for j in range(c):
        if data[i][j] != '#':
            word += data[i][j] # '#'이 아니라면 더하기
        else: # '#'을 만난경우 만들어진 문자가 2글자 이상인지 검사
            # 2글자 이상이라면 words에 삽입
            if len(word) >= 2:
                words.append(word)
            word = '' # word 초기
    if len(word) >= 2:
        words.append(word)
# 세로로 만들 수 있는 문자 삽입
for i in range(c):
    word = ''
    for j in range(r):
        if data[j][i] != '#':
            word += data[j][i] # '#'이 아니라면 더하기
        else: # '#'을 만난경우 만들어진 문자가 2글자 이상인지 검사
            # 2글자 이상이라면 words에 삽입
            if len(word) >= 2:
                words.append(word)
            word = '' # word 초기
    if len(word) >= 2:
        words.append(word)

# 정렬했을때 가장 먼저 오는 문자 출력
print(sorted(words)[0])


