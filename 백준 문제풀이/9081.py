# https://www.acmicpc.net/problem/9081
'''
주어진 단어들로 만들 수 있는 모든 단어 조합에서, 해당 단어의 바로 다음에 등장할 단어 출력
=> 백트래킹, 문자열
'''
def dfs(depth,curr_word):
    global used,result,find
    # 재귀 종료 조건
    if depth == len(word):
        # 기존 문자에 도달하였다면
        if curr_word == ''.join(word):
            find = True
            return
        if find: # 기존 문자에 도달하고 난 직후 다음 문자에 도달하였다면
            result = curr_word
            find = False
            return
    
    for i in range(len(word_list)):
        if not used[i]: # i번째 글자를 아직 사용한 적 없다면
            used[i] = True # 사용처리
            dfs(depth+1,curr_word+word_list[i])
            used[i] = False # 백트래킹

for _ in range(int(input())):
    word = list(input()) # 특정 단어 입력받기
    word_list = sorted(word)
    used = [False for _ in range(len(word))]
    result = ''
    find = False
    dfs(0,'')
    if result == '':
        print(''.join(word))
    else:
        print(result)