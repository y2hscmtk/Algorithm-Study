# https://www.acmicpc.net/problem/1544
'''
같은 단어끼리 같은 단어 그룹에 속하게 한다.
=> 같은 단어는 회전했을때 똑같이 읽을 수 있는지로 판별
=> 우선 단어의 길이가 같은지 확인, 단어의 길이가 같다면 회전시켜보기
기존에 존재하는 단어 그룹에 속할 수 있는지 확인하고, 속할 수 없다면 새로운 단어 그룹으로 만든다.
만들어진 단어 그룹의 개수가 정답
'''
n = int(input())
words = []
for _ in range(n):
    words.append(input())

group = [[words[0]]] # 만들어질 단어 그룹 => 첫번째 단어를 넣고 시작
for word in words: # 단어 그룹에서 단어 한 개를 뽑는다.
    # 그룹에 속해있는 단어에 대해서 같은 단어인지 확인한다.
    find = False
    for group_word in group:
        if find:
            break # 찾았다면 더이상 반복할 필요 없음
        if group_word:
            g_word = group_word[0] # 비교 대상이 될 단어 선별
            # 길이가 같은지 확인
            if len(g_word) != len(word): # 길이가 다르다면, 같은 단어가 될 수 없음
                continue
            g_word*=2 # 회전확인을 위해 이어붙인다.
            if word in g_word: # 포함된다면 => 회전시켰을때 똑같이 읽을 수 있다는 의미
                find = True # 일치하는 그룹을 찾았다는 의미
                continue
    # 일치하는 그룹을 찾지 못했다면 새로운 그룹 생성
    if not find:
        group.append([word])
            

# 만들어진 단어 그룹의 수가 정답 => 모두 같은 단어 일 수 있으므로
if len(group) == 1:
    print(0)
else:
    print(len(group))