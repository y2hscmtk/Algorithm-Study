# 민식이는 수학학원에서 단어 수학 문제를 푸는 숙제를 받았다.

# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.

# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 두 수의 합은 99437이 되어서 최대가 될 것이다.

# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하시오.

# 아이디어 : 같은 자리수가 되기 전까지 9부터 차례로 값을 대입, 같은 자리수부터는 단어의 길이가 긴 단어부터 차례로 값을 대입한다.


n = int(input())  # 단어의 개수 입력받기

word = []  # 입력받은 단어를 저장할 리스트

word_data = [-1]*26  # 값을 할당받지 못한 문자는 -1으로 할당한다.

max_sum = 0  # 최대값을 저장하기 위한 변수
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 단어를 입력받는 단계
for i in range(n):
    word.append(list(input()))  # 각각의 단어를 단어별로 구별하기 위해 리스트 형태로 입력받는다.

word.sort()  # 먼저 알파벳 순으로 정렬을 한다.

# 단어의 글자 길이 순으로 변경하는 과정
for i in range(n):
    for j in range(1, n):
        if len(word[j-1]) < len(word[j]):
            word[j-1], word[j] = word[j], word[j-1]  # 위치 변경

size = 9
# print(ord('A')-65) = 0 # ord() 아스키코드 변환 함수
for i in range(1, n):
    # 두번째로 길이가 긴 단어의 길이전까지 값을 대입한다.
    for j in range(len(word[i-1])-len(word[i])):
        # 아직 값을 할당 받지 못한 경우 해당 알파벳의 위치에 값을 대입해준다.
        if word_data[ord(word[i-1][j])-65] == -1:
            word_data[ord(word[i-1][j])-65] = size
            word[i-1][j] = size
            size -= 1  # 다음 단어는 size--인 값을 대입해준다.
        else:
            # 이미 단어 데이터에 값이 할당되어 있다면, 그 값을 불러와 할당시킨다.
            word[i-1][j] = word_data[ord(word[i-1][j])-65]

# 값을 할당받지 못한 나머지 알파벳에 대해 값을 할당하는 과정
start = len(word[0])-len(word[1])
for i in range(1, n):
    # if word[i][k] not in number:

    # for j in range(start, len(word[i-1])):
    if word[i-1][start] not in number:
        # 단어 데이터에 해당 단어가 있는지 확인
        if word_data[ord(word[i-1][start])-65] != -1:  # -1이 아니라면? => 이미 값이 할당되어 있다면?\
            word[i -
                 1][start] = word_data[ord(word[i-1][start])-65]  # 할당되어있는값으로 변환
        else:
            word_data[ord(word[i-1][start])-65] = size
            word[i-1][start] = size
            size -= 1


print(word)
# print(max_sum)
