# HashMap / 대응되는 수와 문자
'''
n개의 문자열이 주어집니다. 각 문자열은 1부터 n까지 주어진 순서대로 각각 하나의 숫자와 대응됩니다.
이 후, 조사할 m개의 숫자 혹은 문자열이 주어졌을 때, 숫자에 대해서는 대응되는 문자열을, 문자열에 대해서는 대응되는 숫자를 출력하는 프로그램을 작성해보세요.

각 숫자와 문자는 1대1로 대응 -> dict 2개 사용
'''
n,m = map(int,input().split())

word_to_num = {} # 문자와 대응되는 숫자
num_to_word = {} # 숫자와 대응되는 문자

for num in range(1,n+1):
    word = input()
    word_to_num[word] = str(num)
    num_to_word[str(num)] = word 


# 조사할 문자 또는 숫자
for _ in range(m):
    data = input()
    if data in word_to_num:
        print(word_to_num[data])
    elif data in num_to_word:
        print(num_to_word[data])