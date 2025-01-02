# 순서를 바꾸었을 때 같은 단어 그룹화하기
'''
n개의 단어가 입력으로 주어질 때, 
한 단어에 속한 문자들의 순서를 바꾸어 만들 수 있는 단어들은 같은 그룹에 속한다고 정의된다고 합니다. 
이 때 동일한 그룹에 속한 단어가 가장 많은 그룹의 단어 개수를 출력하는 코드를 작성해보세요.
'''
n = int(input())
words = [input() for _ in range(n)]

'''
아이디어 : 등장한 알파벳을 기준으로 새로운 '키'를 만들어 개수 증가
이후 가장 많이 등장한 그룹의 단어 개수 출력
'''
count = dict()
result = 0
# O(1000^1000)
for word in words:
    word_dict = dict()
    key = []
    for a in word:
        if a in word_dict:
            word_dict[a] += 1
        else:
            word_dict[a] = 1
            key.append(a)
    # 키 만들기
    key.sort()
    word_key = ""
    for k in key:
        word_key += (k + str(word_dict[k]))
    
    if word_key in count:
        count[word_key] += 1
    else:
        count[word_key] = 1
    result = max(result, count[word_key]) # 가장 많이 등장한 키 개수 업데이트

print(result)
